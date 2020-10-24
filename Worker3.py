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
while True:
    if not connected:
        conn, addr = server.accept()
        print(f"{addr} CONNECTED TO SERVER")
        connected = True
        continue
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg.upper() == DISCONNECT_MESSAGE:
            print(f"{addr} DISCONNECT FROM SERVER")
            response = f"DISCONNECT FROM SERVER WORKER 3 {ADDR}"
            conn.send(response.encode(FORMAT))
            connected = False
            continue

        # lst = list(map(int, msg.split(",")))
        # lst.sort()

        if len(msg) < 1:
            var_print = f"Error, no input"
            conn.send(var_print.encode(FORMAT))
        elif msg.upper() != DISCONNECT_MESSAGE:
            var = sort_list(msg)
            print(f"[{addr}] {var}")
            var_print = f"SORTED LIST: {var}"
            conn.send(var_print.encode(FORMAT))
        else:
            connected = False

conn.close()
