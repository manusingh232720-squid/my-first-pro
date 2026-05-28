import random
"""1 for rock
2 for scissor
3 for paper
"""

computer=random.choice([1,2,3])
youw=input("enter your weapon:")
yourg={"r":1,"s":2,"p":3}
reverseg={1:"Rock",2:"scissor",3:"paper"} 
you=yourg[youw]

print(f"you choose {reverseg[you]}\n computer choose r{reverseg[computer]}")

if computer==you:
    print("draw")
else:
    if (computer==1 and you==2):
        print("you loss")
    elif(computer==2 and you==1):
        print("you win")
    elif(computer==3 and you==1):
        print("you loss")
    elif(computer==1 and you==3):
        print("you win")
    elif(computer==2 and you==3):
        print("you loss")
    elif(computer==3 and you==2):
        print("you win")
    else:
        print("something is wrong")