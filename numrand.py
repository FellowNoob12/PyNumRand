import random

welcomeMessage = """
------------------------------------
|                                  |
|  Welcome to the Number Guesser!  |
|                                  |
------------------------------------
"""

print(welcomeMessage)

def Function():
    amount = int(input("\nHow large is the number do you want? \n"))
    global answer
    answer = int(input("What is the number the computer randomly picked? \n"))
    global num
    num = random.randint(0, amount)
    
Function()

if answer == num:
    print("You got the correct answer!")
    Function()
else:
    print("You got it wrong.")
    ans = input("\nDo you want to continue? \n")
    if ans == "No":
        pass
    else:
        Function()
        