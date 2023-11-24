"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Server:
"""

# -----------------------------------------------------------------------------------------------
#  imports:
from server import initUDPServer
from game import initGame

# -----------------------------------------------------------------------------------------------

def main():
    initUDPServer()
    initGame()

if __name__ == "__main__":
    main()
