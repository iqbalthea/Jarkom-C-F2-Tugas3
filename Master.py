import socket

HEADER = 2048
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"
SERVER = socket.gethostbyname(socket.gethostname())

# ADDR_1 = ("54.159.86.93", 5051)
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
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    recv_msg = client.recv(2048).decode(FORMAT)
    print(f"{recv_msg}")


def closeAll():
    client_1.close()
    client_2.close()
    client_3.close()


def send(client, msg):
    print(f"JOB IS RUNNING")
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    recv_msg = client.recv(2048).decode(FORMAT)
    if recv_msg == "ERROR":
        print(f"JOB IS FAILED")
    else:
        print(f"JOB IS FINISHED")
<<<<<<< HEAD
        print(f"OUTPUT : {recv_msg}")
=======
        print(f"[OUTPUT] = {recv_msg}")
    
    
>>>>>>> 3749ce02ad912ccbe0b0e6d72d8049775805588c


# connected = True
# while connected:

#     var = input()
#     send(client_1, var)
#     if var.upper() == DISCONNECT_MESSAGE:
#         connected = False
#         continue
