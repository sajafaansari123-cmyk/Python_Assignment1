import random

def welcome():
    
    print("=" * 50)
    print(" Welcome to Number Guessing Game!")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print("=" * 50)

def play_game():
    
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed = False
    
    while not guessed:
        
        guess = int(input("\nEnter your guess: "))
        attempts += 1
        
        
        if guess < secret_number:
            print("LOWER.")
        elif guess > secret_number:
            print("HIGHER.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            guessed = True

def play_again():
    """Ask if player wants to play again"""
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    return choice == "yes" or choice == "y"

def main():
    """Main program"""
    welcome()
    
    playing = True
    
    while playing:
        play_game()
        playing = play_again()
    
    print("Thanks for playing! Goodbye!See you again!")


if __name__ == "__main__":
    main()