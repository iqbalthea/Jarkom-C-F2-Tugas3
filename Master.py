import socket

HEADER = 2048
# PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"
# # SERVER = "18.212.111.142"
SERVER = socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER, PORT)

ADDR_1 = (SERVER, 5051)
ADDR_2 = (SERVER, 5052)
ADDR_3 = (SERVER, 5053)

client_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_1.connect(ADDR_1)

client_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_2.connect(ADDR_2)

client_3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_3.connect(ADDR_3)

print(f"CONNECTED TO SERVER {client_1.getsockname()}")
print(f"CONNECTED TO SERVER {client_2.getsockname()}")
print(f"CONNECTED TO SERVER {client_3.getsockname()}")


def send(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# connected = True
# while connected:

#     var = input()
#     send(client_1, var)
#     if var.upper() == DISCONNECT_MESSAGE:
#         connected = False
#         continue
