connect = True

while(connect):
    user_input = input(">>> ").split()
    command = user_input[0].upper()
    length = len(user_input)

    if length > 2:
        print("Invalid Command")
        continue

    if command == "EXIT":
        connect = False
    elif command == "W1":
        if length != 2:
            print("Invalid Command")
            continue
        print(f"Jobs W1 Saved {user_input[1]}")
    else:
        print("Invalid Command")
        continue
