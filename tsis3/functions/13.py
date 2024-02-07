import random 
x=random.randint(1,20)
t=0
print("Hello! What is your name?")
name=input()
print("Well,", name, "I am thinking of a number between 1 and 20. Take a guess.")
while True:
    y=int(input())
    if (y==x):
        t+=1
        print("Good job, KBTU! You guessed my number in", t, "guesses!")
        break
    elif(y>x):
        t+=1
        print("Your guess is too high.Take a guess.")
    
    elif(y<x):
        t+=1
        print("Your guess is too low.Take a guess.")