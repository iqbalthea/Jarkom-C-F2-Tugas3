import socket
import threading
import test
import time

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

def count_word(x):
    lst = list(map(str, x.split(",")))
    # lst = list(str, x.split())
    # print(lst)
    file_name = lst[0]
    word = lst[1]
    file  = open(f'{file_name}.txt', 'r').read()
    time.sleep(30)
    count = file.count(word)

    return(count)

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
            response = f"DISCONNECT FROM SERVER WORKER 1 {ADDR}"
            conn.send(response.encode(FORMAT))
            connected = False
            continue

        else:
            try:
                # file = input("Enter the name of file: ")
                # word = input("Enter the word: ")

                var = f"Number of words in file: {count_word(msg)}"
            except:
                var = f"ERROR"
        conn.send(var.encode(FORMAT))

conn.close()
