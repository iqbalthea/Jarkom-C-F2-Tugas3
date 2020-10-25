import socket

HEADER = 2048
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "3.84.7.20"
SERVER = "54.237.193.137"

ADDR_1 = (SERVER, 5051)
ADDR_2 = (SERVER, 5052)
ADDR_3 = (SERVER, 5053)

client_1 = None
client_2 = None
client_3 = None


def connect(client, addr):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    print(f"CONNECTED TO SERVER {addr}")
    return client


def disconnect(client):
    msg = DISCONNECT_MESSAGE
    message = msg.encode(FORMAT)
    client.send(message)
    recv_msg = client.recv(HEADER).decode(FORMAT)
    print(f"{recv_msg}")
    client.close()


def closeAll(client_1, client_2, client_3):
    try:
        disconnect(client_1)
        print(f"SUCESS DISCONNECT WORKER 1")
    except:
        print(f"FAILED DISCONNECT WORKER 1")
        print(f"Worker 1 is not connected to the server")
    try:
        disconnect(client_2)
        print(f"SUCESS DISCONNECT WORKER 2")
    except:
        print(f"FAILED DISCONNECT WORKER 2")
        print(f"Worker 2 is not connected to the server")
    try:
        disconnect(client_3)
        print(f"SUCESS DISCONNECT WORKER 3")
    except:
        print(f"FAILED DISCONNECT WORKER 3")
        print(f"Worker 3 is not connected to the server")


def send(client, msg):
    print(f"JOB IS RUNNING")
    message = msg.encode(FORMAT)
    client.send(message)
    recv_msg = client.recv(2048).decode(FORMAT)
    if recv_msg == "ERROR":
        print(f"JOB IS FAILED")
    else:
        print(f"JOB IS FINISHED")
        print(f"[OUTPUT] = {recv_msg}")


