from os.path import exists

if exists("name.txt"):

    file = open("name.txt", "r")
    name = file.read()
    file.close()

    if len(name) > 0:
        print("Hello,", name, "!")

else:
    name = input("What is your name?: ")
    file = open("name.txt", "w")
    file.write(name)
    file.close()
    print("Hello", name, "!")