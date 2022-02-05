import random
import art

print(art.logo)
print("Welcome to the 'Guessing Game'\nCan you Guess My Number?")
difficulty = input("Do you want to play in 'Easy' Mode = 10 Tries or 'Hard' Mode = 5 Tries? ").lower().strip()

life = 0

if difficulty == "hard":
    life += 5
else:
    life += 10

computer_number = random.randint(1, 100)
print(f"You have {life} Tries to start. My number to guess is from 1 to 100.")


def guessing_game():
    global life

    flag = True
    while flag:
        if life == 0:
            print("You ran out of lives. Good luck next time.")
            quit()

        player_guess = int(input("What do you guess? "))
        life -= 1
        if player_guess == computer_number:
            flag = False
            break
        elif player_guess > computer_number:
            print("Your guess is too high!\nGuess again.")
            print(f"You have {life} tries remaining.\n")

        else:
            print("Your guess is too low!\nGuess again.")
            print(f"You have {life} tries remaining.\n")

    print(f"You guessed it! The Computer's number was {computer_number}.\nYou win!")
    print(art.logo_congrats)


guessing_game()
