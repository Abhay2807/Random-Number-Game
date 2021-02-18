import random
randomNumber=random.randint(1,100)

userGuess=None
guess=0 
 
for i in range(1,101):
    userGuess=int(input("Enter your guess : "))
    if (userGuess > randomNumber):
        print(" You guessed it wrong! Enter a smaller number") 
    elif(userGuess < randomNumber):
        print("You guessed it wrong! Enter a larger number")
    else:
        print("You guessed it right!")
        guess=i
        break

print(f"You guessed the number in {guess} guesses")

with open("for_hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    print("You have just broken the Best score!")
    with open("for_hiscore.txt", "w") as f:
        f.write(str(guess))

elif int(hiScoreStr)>guess:
    print("You have just broken the Best score!")
    with open("for_hiscore.txt", "w") as f:
        f.write(str(guess))





