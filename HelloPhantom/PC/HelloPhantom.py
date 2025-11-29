from gpt import PhantomGPT
from socketing.socketclient import Client
from socketing.socketserver import Server
import time

class HelloPhantom:

    def start_loop():
        prompt = Server.recieve()

        output = PhantomGPT.PhantomSpeak(prompt)

        Client.send(output[1][1])

    if __name__ == "__main__":
        while True:
            start_loop()
            time.sleep(3)

        



