import random

welcomeMessage = """
------------------------------------
|                                  |
|  Welcome to the Number Guesser!  |
|                                  |
------------------------------------
"""

print(welcomeMessage)
    
while True:
    amount = int(input("How large is the number do you want? \n"))
    answer = int(input("What is the number the computer randomly picked? \n"))
    num = random.randint(0, amount)
    
    if answer is num:
        print("You got the correct answer!")
        continue
    else:
        print("You got it wrong.")
        ask = input("Do you want to exit? \n")
        if ask is "True":
            pass