import random

def autogen():
    correct = random.randint(0,100)
    return correct

correct = autogen()
count = 0
guessed = False

while count < 7:
    num = int(input("Enter a number between 0 to 100:"))
    
    if num == correct:
        print("Your guess is correct!")
        guessed = True
        break
    elif num < correct:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
        
    count += 1

if guessed == False:
    print("You ran out of attempts, the number was:", correct)