from socket import *

HEADER = 1024
PORT_SERVER = 5050
FORMAT = 'utf-8'
SERVER = gethostbyname(gethostname())
ADDR = (SERVER, PORT_SERVER)
DISCONNECT_MESSAGE = "EXIT"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode(FORMAT))
modifiedSentence = clientSocket.recv(HEADER).decode(FORMAT)

print(modifiedSentence)
clientSocket.close()
