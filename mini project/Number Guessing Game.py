import random

def play_game():
    print("\n===== NUMBER GUESSING GAME =====")

    secret_number = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low!")
            elif guess > secret_number:
                print("Too High!")
            else:
                score = max(100 - (attempts - 1) * 10, 10)
                print("\nCongratulations!")
                print("You guessed the correct number.")
                print("Attempts:", attempts)
                print("Score:", score)
                break

        except ValueError:
            print("Please enter a valid number.")
