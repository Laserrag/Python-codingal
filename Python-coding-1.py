secret = 27
attempt = 5
while attempt > 0:
    print("You have", attempt, "attempts left.")
    guess = int(input("Enter your guess: "))
    attempt -= 1
    if guess != secret:   
        if guess >= 10:
            print("Ice cold!🥶")
        elif guess >= 20:
            print("Cold!🧊")
        elif guess >= 25:
            print("Hot! 🔥")
        elif guess > 30:
            print("cold!🧊")
        attempt -= 1
    else:
        print("Congratulations! You guessed the secret number!")
    break
