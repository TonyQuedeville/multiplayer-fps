"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Server UDP:
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import socket

# -----------------------------------------------------------------------------------------------
# globals:

# Adresse IP et port sur lequel le serveur va écouter
serveur_ip = "127.0.0.1"
serveur_port = 12345

# Création d'une socket UDP
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liaison de la socket à l'adresse et au port
serveur_socket.bind((serveur_ip, serveur_port))

# -----------------------------------------------------------------------------------------------

def initUDPServer():
    print(f"Serveur UDP en attente sur {serveur_ip}:{serveur_port}")

    while True:
        # Recevoir les données du client
        donnees, adresse_client = serveur_socket.recvfrom(1024)
        
        # Afficher les données reçues
        print(f"Reçu depuis {adresse_client}: {donnees.decode('utf-8')}")
        
        # Envoie d'une réponse au client
        message_confirmation = "Message reçu avec succès!"
        serveur_socket.sendto(message_confirmation.encode('utf-8'), adresse_client)
