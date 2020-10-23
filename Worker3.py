import socket
import threading

HEADER = 2048
PORT = 5053
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


def sort_list(x):
    lst = list(map(int, x.split(",")))
    lst.sort()
    return lst

connected = True
while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg.upper() == DISCONNECT_MESSAGE:
            connected = False
            continue

        # lst = list(map(int, msg.split(",")))
        # lst.sort()

        var = sort_list(msg)

        if len(var) < 1:
            var = f"Error, no input"
            conn.send(var.encode(FORMAT))
        elif msg.upper() != DISCONNECT_MESSAGE:
            print(f"[{addr}] {var}")
            var_print = f"Sorted list: {var}"
            conn.send(var_print.encode(FORMAT))
        else:
            connected = False

conn.close()
