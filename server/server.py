"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Server UDP:
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import socket, pickle
import netifaces as ni
from game import Game

# -----------------------------------------------------------------------------------------------
# globals:

# Adresse IP et port sur lequel le serveur va écouter
serveur_ip = ""
serveur_port = 12345

# -----------------------------------------------------------------------------------------------

# Recupération de l'adresse ip du server. equivaux à BASH get ip: ip a | grep 'inet.*brd' | awk '{print $2}' | cut -f1 -d'/'
def get_ip_address():
    try:
        interfaces = ni.interfaces()
        for interface in interfaces:
            addresses = ni.ifaddresses(interface)
            if ni.AF_INET in addresses:
                for address in addresses[ni.AF_INET]:
                    if 'broadcast' in address:
                        return address['addr']
        return None
    except Exception as e:
        print("Error:", e)
        return None

def broadcast(serveur_socket, game, data, serveur_ip, id_client):
    for player in game.players:
        if player.id != id_client:
            serialized_msg = pickle.dumps(data)
            serveur_socket.sendto(serialized_msg, (serveur_ip, player.id_client))

def send_self(serveur_socket, serveur_ip, id_client, data):
    serialized_msg = pickle.dumps(data)
    serveur_socket.sendto(serialized_msg, (serveur_ip, id_client))

def initUDPServer():
    serveur_ip = get_ip_address()

    # Création d'une socket UDP
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Liaison de la socket à l'adresse et au port
    serveur_socket.bind((serveur_ip, serveur_port))

    print(f"Serveur UDP en attente sur {serveur_ip} : {serveur_port}")
    game = Game()
    
    while True:
        data = None
        
        # Reception des données client
        serial_data, adress_client = serveur_socket.recvfrom(2048)
        id_client = adress_client[1]
        received_data = pickle.loads(serial_data)  # Désérialiser les données binaires reçues
        
        pseudo = ""
        # Joueur entrant
        if "pseudo" in received_data:            
            # Envoi de l'ajout du joueur aux autres joueurs
            pseudo = received_data["pseudo"]
            data = game.add_player(id_client, pseudo)
            broadcast(serveur_socket, game, data, serveur_ip, id_client) 
            
            # Envoi des données des autres joueurs pour initialisation
            data = game.init_game(data["addPlayer"]["id"])
            send_self(serveur_socket, serveur_ip, id_client, data)
        
        # Joueur sortant
        if "quit" in received_data:
            data = game.sup_player(id_client)
            send_self(serveur_socket, serveur_ip, id_client, data)
        
        # Joueur joue
        if "play" in received_data:
            data = game.update_player(id_client, received_data["play"])
            broadcast(serveur_socket, game, data, serveur_ip, id_client)
            
        # Joueur prend un médaillon
        if "take_token" in received_data:
            data = game.update_tokens(id_client, received_data["take_token"])
            broadcast(serveur_socket, game, data, serveur_ip, None)

