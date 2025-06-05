import random
print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
while True:
    num=random.randint(1,100)
    n=5
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    while True:
        try:
            ch=int(input("Enter choice:"))
            if ch<=3 and ch>0:
                break
            else:
                print("Please select a valid choice")
        except ValueError:
            print("Please enter a number")
    if ch==1:
        n=10
        print("Great! You have selected the Easy difficulty level.")
    elif ch==3:
        n=3
        print("Great! You have selected the Hard difficulty level.")
    else:
        print("Great! You have selected the Medium difficulty level.")
    print("Let's start the game!")
    tries=0
    won=False
    while n>0:
        guess=int(input("Enter your guess:"))
        if guess>num:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess<num:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Congratulations! You guessed the correct number in {tries} attempts.")
            won=True
            break
        n-=1
        tries+=1
    if  won==False:
        print(f"Tough Luck! the number was {num}.")
    again=input("Want to play again(y/n):")
    if again=='n':
        print("Thanks for playing, hope to see you again!")
    elif again=='y':
        print("Here We Go Again!")
    else:
        print("Oh look you accidentally pressed yes")



    