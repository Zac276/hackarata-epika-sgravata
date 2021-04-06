import socket
import os
import mouse

#dati per la conneessione e altro
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())# gethostbyname prende l'ip dell'host con il nome specificato fra parentesi, e il nome lo trova con gethostname
ADDR = (SERVER, PORT)#ipv4+porta
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#crea nuovo soket IMPORTANT : AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family, and then you can only use addresses of that type with the socket.
server.bind(ADDR)#lega il socket sopra creato all'address specificato (deve essere della stessa address family per comunicare in questo caso ipv4)

x=[]
y=[]
def handle_client(conn, addr): 
    
    try:
        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT) #decodifica il messaggio (byte--->string)
            if msg_length: #se il messaggio ha un contenuto
                msg_length = int(msg_length)#numero di bit da aspettarsi come lunghezza del messaggio
                msg = conn.recv(msg_length).decode(FORMAT)#nelle parentesi di "recv()" ci si mettono il numero di bit sopra trovato, poi decodifica i bit con il format "utf-8"
                x,y=eval(msg)
                mouse.move(x,y)
                print(f"[{addr}] {msg}")
    
    except:
        print("[DISCONNECTED] client disconnected")
            
    
    conn.close


server.listen()
print(f"server in ascolto, ip : {SERVER}, port : {PORT}")
conn, addr = server.accept()
print(f"Connessione stabilita address : {addr}")
handle_client(conn,addr)

