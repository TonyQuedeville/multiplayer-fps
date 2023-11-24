"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Server UDP:
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import socket
import threading

# -----------------------------------------------------------------------------------------------
# globals:
# Adresse IP et port du serveur
serveur_ip = "127.0.0.1"
serveur_port = 12345

# Message à envoyer au serveur
message = "Hello, serveur UDP!"

# Création d'une socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)  # Définir un timeout de 5 secondes

# -----------------------------------------------------------------------------------------------

def initUDPClient():
    # Démarrer le thread de réception
    thread_reception = threading.Thread(target=recevoir)
    thread_reception.start()

    try:
        while True:
            # Saisie du message depuis l'utilisateur
            message = input("Entrez votre message (ou 'exit' pour quitter) : ")
            
            # Envoi du message au serveur
            client_socket.sendto(message.encode('utf-8'), (serveur_ip, serveur_port))

            if message.lower() == 'exit':
                break  # Sortir de la boucle si l'utilisateur entre 'exit'
            
            try:
                # Réception de la réponse du serveur avec un timeout
                confirmation, _ = client_socket.recvfrom(1024)
                print(f"Confirmation du serveur : {confirmation.decode('utf-8')}")
            except socket.timeout:
                print("Timeout : Aucune confirmation reçue dans le délai spécifié.")


    except KeyboardInterrupt:
        print("\nClient interrompu par l'utilisateur.")

    finally:
        # Attendre que le thread de réception se termine avant de fermer la socket
        thread_reception.join()
        client_socket.close()

def recevoir():
    while True:
        # Réception de la réponse du serveur
        confirmation, _ = client_socket.recvfrom(1024)
        print(f"Confirmation du serveur : {confirmation.decode('utf-8')}")