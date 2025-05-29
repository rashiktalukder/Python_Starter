
def GuessTheNumber():
    setNumber = 8
    guessingNumber = int(input("Guess The Number:"))

    if guessingNumber > setNumber:
        return "your guess is higher"
    elif guessingNumber < setNumber:
        return "your guess is almost there"
    else:
        return "Your Guess Is Correct!"

print(GuessTheNumber())
