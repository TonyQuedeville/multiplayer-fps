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

# -----------------------------------------------------------------------------------------------
# globals:
# Adresse IP et port du serveur
serveur_ip = "192.168.1.46" #"192.168.100.151" #"127.0.0.1"
serveur_port = 12345

# Création d'une socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)  # Définir un timeout de 5 secondes

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
    # print("serveur_ip:", serveur_ip)
    print("data:", data)
    
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
    while True: # Ecoute serveur
        # Réception de la réponse du serveur
        data, adress_server = client_socket.recvfrom(1024)
        # print("adress_server:", adress_server)
        received_data = pickle.loads(data)  # Désérialiser les données binaires reçues
        return received_data

def initUDPClient():
    serveur_ip = get_ip_address() # Recupère l'ip pour les tests: à enlever en prod.
    
    # Saisie du message depuis l'utilisateur
    pseudo = new_player()
    if not pseudo == None:
        send_sever(pseudo)

    # Démarrer le thread de réception
    thread_reception = threading.Thread(target=listen_server)
    thread_reception.start()

    if not initIHM(serveur_port, serveur_ip, client_socket):
        send_sever({"quit" : pseudo["pseudo"]})
        
        thread_reception.join()
        client_socket.close()

