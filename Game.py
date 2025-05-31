import random
print("WELCOME TO NUMBER GUESSING GAME")
t='y'
count=1
w=0
l=0
while t!='n':
    n=int(input("Please enter the range for guess: "))
    x=random.randint(1,n)
    p=int(input("Now enter your guess: "))
    if p==x:
        w+=1
        print(f"congratulations, you're right, it is {x}")
    else:
        l+=1
        print("sorry, tough luck")
    t=input("wanna try again(y/n):")
    if t=='y':
        count+=1
        print(f"okay round {count}")
print("Thanks for playing :)")
print(f"you played {w+l} times and won {w} times")
