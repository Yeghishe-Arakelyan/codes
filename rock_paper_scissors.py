import random 

def get_computer_choice():
    # Function to get a random choice for the computer (rock, paper, or scissors)
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # Function to get the user's choice and validate it
    while True:
        user_choice = input('Enter your choice (rock, paper, scissors): ')
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    # Function to determine the winner of each round
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'
    
def play_game():
    # Main function to play the Rock-Paper-Scissors game
    computer_score = 0
    user_score = 0
    
    while computer_score < 3 and user_score < 3:
        print("Let's play Rock-Paper-Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()  

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "draw":
            print(f"It's a draw. Computer score: {computer_score}, Your score: {user_score}")
        elif result == "win":
            user_score += 1
            print(f"Congratulations, you win! Computer score: {computer_score}, Your score: {user_score}")
        else:
            computer_score += 1
            print(f"Sorry, you lose. Computer score: {computer_score}, Your score: {user_score}")
        
        if computer_score == 3 or user_score == 3:
            print('End game.')

play_game()
