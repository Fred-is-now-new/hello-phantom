import socket
#import threading

HEADER = 64
#gets this computer's addresses as variables
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

#test command to get the name of this device
#print(socket.gethostname())

#initializes the server and binds it to this address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#actually interacts witht the connection
def handle_client(conn, addr):
    print(f"New Connection: {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            
            msg = conn.recv(msg_length)
            print(f"Connection: {addr}; Message: \n{msg}")
            connected = False
    
    conn.close()
    print(f"Connection Severed: {addr} disconnected.")
    return 0






#opens this computer as a server and gets the ip connection, then passes any connections into handle_client()
def start():
    #'listens' for new connections, stores them as a websocket (conn) and ip (addr)
    server.listen()
    print(f"Server is listening from {SERVER}")
    while True:
        conn, addr = server.accept()
        
        #then makes a seperate thread to handle it
        #thread = threading.Thread(target=handle_client, args=(conn, addr))
        #thread.start()

        handle_client(conn, addr)
        
        #test print to check active connections
        #print(f"ACTIVE CONNECTIONS: {threading.active_count() - 1}")


print(f"{socket.gethostname()} server is starting...")
start()