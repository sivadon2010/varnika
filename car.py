cammand = ""
started = False
while True:
    cammand = input(">").lower()
    if cammand == "start" :
        if started:
            print("car is aldready started")
        else:
            started = True
            print("car is started")
    elif cammand == "stop" :
        if not started:
            print('car is aldready stopped')
        else :
            started = False
            print("car is stopped")
    elif cammand == "help":
        print("start - to start the car \nstop - to stop the car \nquit - to quit")
    elif cammand == "quit":
        break
    else:
        print("i don't understand your words")
