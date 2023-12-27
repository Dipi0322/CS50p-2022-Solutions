#import modules
import random

#prompt for n
while True:
    try:
        n = int(input("Level: "))
        #if not positive re-prompt
        if n <= 0:
            continue
        else:
            break
    #raise error flag
    except ValueError:
        pass

#programme guessing the value
x = random.randint(1,n)

#user's guess
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
        if guess < x:
            print("Too small!")
            continue
        elif guess > x:
            print("Too large!")
            continue
        elif guess == x:
            print("Just right!")
            break
    #error flag if user enters different value
    except ValueError:
        continue
