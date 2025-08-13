import random

num = random.randint(1, 33)
flag = True
guess = 0

print("Guess my number 1-33: ", end= " ")
while flag :                 # while flag remains True.
    
    guess = input()
    if not guess.isdigit() :
        print("Invalid! Enter only digits 1-33", end = " ")
    elif int(guess) < num :
        print("Too low, try again: ", end = " ")
    elif int(guess) > num :
        print("Too high, try again: ", end = " ")
    else :
        print("Correct... My number is " + guess)
        flag = False
