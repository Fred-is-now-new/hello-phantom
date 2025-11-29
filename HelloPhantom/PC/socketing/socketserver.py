import socket


class Server:
    def recieve():
        HEADER = 64
        PORT = 5050
        SERVER = socket.gethostbyname(socket.gethostname())
        #SERVER = "192.168.8.1"
        ADDR = (SERVER, PORT)
        FORMAT = 'utf-8'
        DISCONNECT_MESSAGE = '!DISCONNECT'

        output = ""

        if not hasattr(socket, 'SO_REUSEPORT'):
            socket.SO_REUSEPORT = 15

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        #server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        
        server.listen()
        print(f"Server is listening from {SERVER}")
        
        conn, addr = server.accept()
        
        print(f"New Connection: {addr} connected")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                
                msg = conn.recv(msg_length)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                else:
                    print(f"Connection: {addr}; Message: \n{msg}")
                    output = str(msg)[2:(len(str(msg))-1)]
                    #output = str(msg)
                    connected = False
        
        conn.close()
        print(f"Connection Severed: {addr} disconnected.")
        server.close()
        return output

    if __name__ == "__main__":
        print("Output: " + recieve())
            
            
        





