import random

welcomeMessage = """
------------------------------------
|                                  |
|  Welcome to the Number Guesser!  |
|                                  |
------------------------------------
Do q or quit to quit.
"""

print(welcomeMessage)

def Function():
    try:
       amount = int(input("\nHow large is the number do you want? \n"))
       global answer
       answer = int(input("What is the number the computer randomly picked? \n"))
       global num
       num = random.randint(0, amount)
    except:
        answer = str()
        num = str()
    
Function()

try:
   if answer == num:
    print("You got the correct answer!")
    Function()
   else:
    print("You got it wrong.")
    ans = input("\nDo you want to continue? \n")
    
except:      
   if answer or num == "q" or "quit":
    quit()
        