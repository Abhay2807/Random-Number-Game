import random
randomNumber = random.randint(1,100)


userGuess = None
guess = 0

while(userGuess != randomNumber):
    userGuess = int(input("Please Enter your guess: "))
    guess += 1
    if(userGuess==randomNumber):
        print("You guessed it right!")
    elif(userGuess>randomNumber):
        print("You guessed it wrong! Enter a smaller number")
    else:
        print("You guessed it wrong! Enter a larger number")

print(f"You guessed the correct number in {guess} guesses")

with open("while_hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    print("You have just broken the Best score!")
    with open("while_hiscore.txt", "w") as f:
        f.write(str(guess))

elif int(hiScoreStr)>guess:
    print("You have just broken the Best score!")
    with open("while_hiscore.txt", "w") as f:
        f.write(str(guess))
