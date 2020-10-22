from Master import *

connect = True

while(connect):
    user_input = input(">>> ").split()
    command = user_input[0].upper()
    length = len(user_input)

    if length != 2:
        print("Invalid Command")
        continue

    argument = user_input[1]

    if command == "EXIT" and argument == "ALL":
        connect = False
    elif command == "W1":
        send(client_1, argument)
    elif command == "W2":
        send(client_2, argument)
    elif command == "W3":
        send(client_3, argument)
    else:
        print("Invalid Command")
        continue


send(client_1, DISCONNECT_MESSAGE)
send(client_2, DISCONNECT_MESSAGE)
send(client_3, DISCONNECT_MESSAGE)
client_1.close()
client_2.close()
client_3.close()
