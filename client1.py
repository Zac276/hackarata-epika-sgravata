import socket
import os
import pyautogui

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "172.21.208.1" #cambia a seconda di dove runni il server
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_msg(msg):
    
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length +=b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def recive_msg():
    connected=True
    while connected:
        msg=client.recv(2048).decode(FORMAT)
        if msg:
            print(msg)

client.connect(ADDR)
while True:
    x,y=pyautogui.position()
    coord=(x,y)
    mess=str(coord)
    send_msg(mess)
