from Master import *

connected = True
status_W1 = False
status_W2 = False
status_W3 = False

while connected:
    user_input = input(">>> ").split()
    length = len(user_input)

    if length != 2:
        print("Invalid Command")
        continue
    
    command = user_input[0].upper()
    argument = user_input[1]

    if command == "EXIT" and argument == "ALL":
        connected = False
        closeAll()
    elif command == "W1":
        if argument.upper() != "CONNECT" and not status_W1:
            print(f"Not connected to W1")
        elif argument.upper() == "CONNECT" and not status_W1:
            try :
                connect(client_1, ADDR_1)
                status_W1 = True
                continue
            except :
                reconnect(ADDR_1)
                status_W1 = True
        elif argument.upper() == "DISCONNECT" and status_W1:
            disconnect(client_1)
            status_W1 = False
        else:
            send(client_1, argument)
    elif command == "W2":
        if argument.upper() != "CONNECT" and not status_W2:
            print(f"Not connected to W2")
        elif argument.upper() == "CONNECT" and not status_W2:
            try :
                connect(client_2, ADDR_2)
                status_W2 = True
            except :
                reconnect(ADDR_2)
                status_W2 = True
        elif argument.upper() == "DISCONNECT" and status_W2:
            disconnect(client_2)
            status_W2 = False
        else:
            send(client_2, argument)
    elif command == "W3":
        if argument.upper() != "CONNECT" and not status_W3:
            print(f"Not connected to W3")
        elif argument.upper() == "CONNECT" and not status_W3:
            try :
                connect(client_3, ADDR_3)
                status_W3 = True
            except :
                reconnect(ADDR_3)
                status_W3 = True
        elif argument.upper() == "DISCONNECT" and status_W3:
            disconnect(client_3)
            status_W3 = False
        else:
            send(client_3, argument)
    else:
        print("Invalid Command")
        continue
