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
# BASH get ip: ip a | grep 'inet.*brd' | awk '{print $2}' | cut -f1 -d'/'
serveur_ip = "127.0.0.1"
serveur_port = 12345

# -----------------------------------------------------------------------------------------------

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

def initUDPServer():
    serveur_ip = get_ip_address()

    # Création d'une socket UDP
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Liaison de la socket à l'adresse et au port
    serveur_socket.bind((serveur_ip, serveur_port))

    print(f"Serveur UDP en attente sur {serveur_ip} : {serveur_port}")
    game = Game()
    
    while True:
        message = None
        
        # Reception des données client
        data, adress_client = serveur_socket.recvfrom(1024)
        id_client = adress_client[1]
        received_data = pickle.loads(data)  # Désérialiser les données binaires reçues
        print(received_data)
        
        pseudo = ""
        # Joueur entrant
        if "pseudo" in received_data:
            pseudo = received_data["pseudo"]
            message = game.add_player(id_client, pseudo)
            print("nb players:", len(game.players))
        
        # Joueur sortant
        if "quit" in received_data:
            pseudo = received_data["quit"]
            message = game.sup_player(id_client, pseudo)
            print("nb players:", len(game.players))
        
        # Joueur joue
        if "play" in received_data:
            message = game.update_player(id_client, received_data["play"])        
        
        # Envoi de la reponse au client
        print("send message:", message)
        if message:
            serialized_msg = pickle.dumps(message)
            serveur_socket.sendto(serialized_msg, adress_client)
