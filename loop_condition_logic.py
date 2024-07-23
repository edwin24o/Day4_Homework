#Task1
while True:
    walk = input("You are walking. Type 'stop' to stop walking: ")
    if walk.lower() == 'stop':
        print("You have stopped walking")
        break
    else:
        print("You have stopped walking.")

#Task2

birds = []
while len(birds) < 5:
    print("A freightened mouse running because..")
    birds.append('1')
    print("There are", len(birds), "eagles locked in for the hunt")
