#9/7/25
#s.n

name = input("What is your name? ")
print("Hello:",name)
answer = input("Do you you like sports?")
if answer.lower() == "yes":
    print("which ones?")
    pickOne = input("What is your favourite sport?")
    if pickOne.lower() == "basketball":
        print("That one is cool")
    elif pickOne.lower() == "football":
        print("That one is pretty cool")
    else:
        print("That one is ok")
else:
    print("Oh ok, that's cool too.")