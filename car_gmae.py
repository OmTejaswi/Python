command = ''
started = True
while True:
    command = input(">> ").lower()

    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("start: to start the car. \nstop: to stop the car. \nquit: to quit.")
    elif command == "quit":
        break
    elif command != "start" or command != "stop" or command != "quit" or command != "" or command != "help":
        print("""Sorry, it's isn't a command. Type "help" to see all the commands""")