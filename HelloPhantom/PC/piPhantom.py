from socketing.socketclient import Client
from socketing.socketserver import Server
import time


class piPhantom:
    def runPiLoop():
        Client.send(input("Q: "))
        
        time.sleep(5)

        print(Server.recieve().replace("\n", " "))

    if __name__ == "__main__":
        while True:
            runPiLoop()