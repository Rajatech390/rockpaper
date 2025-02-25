import random

# Function to determine the winner of the round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to play a round of Rock, Paper, Scissors
def play_round():
    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Validate input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return None, None
    
    # Computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chooses: {computer_choice}")
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    return user_choice, result

# Main function to run the game
def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Choose rock, paper, or scissors. Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    
    while True:
        user_choice, result = play_round()

        if user_choice:
            print(f"You chose: {user_choice.capitalize()}")
            print(result)

            # Update scores based on the result
            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1

            # Display the current score
            print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    main()
