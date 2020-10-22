import socket
import threading

HEADER = 2048
PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"SERVER IS LISTENING ON {server.getsockname()}")
conn, addr = server.accept()
print(f"{addr} CONNECTED TO SERVER")

connected = True
while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg.upper() == DISCONNECT_MESSAGE:
            connected = False
            continue

        print(f"[{addr}] {msg}")
        var = f"Hello {msg}"
        conn.send(var.encode(FORMAT))

conn.close()
