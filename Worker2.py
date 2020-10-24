import socket
import threading

HEADER = 2048
PORT = 5052
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"SERVER IS LISTENING ON {server.getsockname()}")


def find_factor(x):
    list_number = []
    x = int(x)
    for i in range(1, x+1):
        if x % i == 0:
            list_number.append(i)
    listToStr = ' '.join([str(i) for i in list_number])
    return listToStr


conn, addr = server.accept()
print(f"{addr} CONNECTED TO SERVER")

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
            response = f"WORKER 2 DISCONNECT FROM SERVER {ADDR}"
            conn.send(response.encode(FORMAT))
            connected = False
            continue
        elif msg.upper() == "CONNECT" :
            var = f"WORKER 2 ALREADY CONNECTED"
        else :
            try :
                var = find_factor(msg)
            except :
                var = f"ERROR"
        conn.send(var.encode(FORMAT))

conn.close()
