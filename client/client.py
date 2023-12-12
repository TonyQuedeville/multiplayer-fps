"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Server UDP:
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import socket, threading, pickle
import netifaces as ni
from ihm import initIHM
from ihm import get_ihm_game

# -----------------------------------------------------------------------------------------------
# globals:
# Adresse IP et port du serveur
serveur_ip = "192.168.1.46" #"192.168.100.151" #"172.16.0.230" # #"127.0.0.1"
serveur_port = 12345

# Création d'une socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

stop_event = threading.Event()

# -----------------------------------------------------------------------------------------------
# Recupere l'ip pour les tests: à enlever en prod.
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
    
def send_sever(data):
    global serveur_ip
    
    if serveur_ip and data:
        serialized_data = pickle.dumps(data)
        client_socket.sendto(serialized_data, (serveur_ip, serveur_port))

def new_player():
    global serveur_ip
    # serveur_ip = input("Entrez l'adresse ip du server (ou 'exit' pour quitter) : ")
    pseudo = input("Entrez votre pseudo (ou 'exit' pour quitter) : ")
    
    if serveur_ip == "exit" or pseudo == "exit":
        return None
    return {"pseudo" : pseudo}

def listen_server():
    client_socket.settimeout(.5)
    
    game = get_ihm_game()
    while not stop_event.is_set(): # Ecoute serveur
        try:
            data, adress_server = client_socket.recvfrom(2048)
            # print("adress_server:", adress_server)
            received_data = pickle.loads(data) # déserialise les données
            
            if received_data:
                # Joueur entrant
                if "addPlayer" in received_data:
                    game.add_player(received_data["addPlayer"])
                if "confirmPlayer" in received_data:
                    game.confirm_player(received_data["confirmPlayer"])
                
                # Joueur sortant
                if "supPlayer" in received_data:
                    game.sup_player(received_data["supPlayer"])
                
                # Joueur joue
                if "play" in received_data:
                    game.update_player(received_data["play"]) 
                
                # Initialisation de l'id du joueur
                if "my_id" in received_data:
                    game.set_me(received_data)
                    
                # Initialisation des joueurs
                if "init_players" in received_data:
                    print("received_data:", received_data["init_players"])
                    game.init_players(received_data["init_players"])
                
                # Initialisation des médaillons
                if "init_tokens" in received_data:
                    game.init_tokens(received_data)
                
                # Changement du score du joueur
                if "change_score" in received_data:
                    game.change_score(received_data["change_score"])
            
        except socket.timeout:
            pass

def initUDPClient():
    # Saisie du message depuis l'utilisateur
    pseudo = new_player()
    if not pseudo == None:
        send_sever(pseudo)

    # Démarrer le thread de jeu
    thread_game = threading.Thread(target=initIHM, args=(serveur_port, serveur_ip, client_socket, pseudo["pseudo"]))
    thread_game.start()

    # Démarrer le thread de réception
    thread_reception = threading.Thread(target=listen_server)
    thread_reception.start()

    # Attente de fin de jeu
    thread_game.join()
    stop_event.set()

