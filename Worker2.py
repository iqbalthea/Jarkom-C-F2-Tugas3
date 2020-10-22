import socket
import threading

HEADER = 2048
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("[STARTING] server is starting...")
conn, addr = server.accept()

def find_factor(x):
    list_number = []
    x = int(x)
    print("Faktor dari", x, "adalah:")
    for i in range(1, x+1):
        if x % i == 0:
            list_number.append(i)
    listToStr = ' '.join(list_number) 
    return listToStr

connected = True
while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")
        var = find_factor(msg)
        conn.send(var.encode(FORMAT))

conn.close()
