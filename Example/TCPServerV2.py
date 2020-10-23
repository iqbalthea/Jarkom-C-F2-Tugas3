from socket import *

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
SERVER = gethostbyname(gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "EXIT"

# Membuat Socket TCP - IPv4
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(ADDR)
serverSocket.listen()
print(f"THE SERVER LISTENING ON {ADDR}")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"CLIENT {addr} CONNECTED ON SERVER")

    sentence = connectionSocket.recv(HEADER).decode(FORMAT)

    print(f"CLIENT SENT MESSAGE {sentence}")
    capitalizedSentence = sentence.upper().encode(FORMAT)

    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
