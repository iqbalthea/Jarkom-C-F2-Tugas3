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
        print(f"[{addr}] {msg}")
        if msg == DISCONNECT_MESSAGE:
            print(f"{addr} DISCONNECT FROM SERVER")
            response = f"DISCONNECT FROM SERVER WORKER 3 {ADDR}"
            conn.send(response.encode(FORMAT))
            connected = False
            continue

        else:
            try:
                var = f"SORTED LIST: {sort_list(msg)}"
            except:
                var = f"ERROR"
        conn.send(var.encode(FORMAT))

conn.close()
