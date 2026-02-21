import random

class RockPaperScissor:
    """Main class for Rock Paper Scissors game.
    """
    def __init__(self, name: str):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choices}): ')
        if user_choice.lower() in self.choices:
            return user_choice 
        print(f'Invalid choice. You must select from {self.choices}')
        return self.get_player_choice() # recursive method

    def get_computer_choice(self):
        """Get computer choice randomly from the list of choices.
        """
        return random.choice(self.choices)

    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Decide the winner of the game.

        :param user_choice: The user's choice.
        :param computer_choice: The computer's choice.
        :return: The result of the game.
        """
        if user_choice == computer_choice:
            return "It's a Tie!"

        win_combinations =[('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'rock')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                return "Congratulations! You won!"

            return "Oh no! You lost!"

    def play(self):
        """Play the game.
        - get user choice
        - get computer choice
        - decide the winner
        - print the result
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"Computer's choice: {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))


# Test case
if __name__ == '__main__':
    game = RockPaperScissor('Sahar')

    while True:
        game.play()

        continue_game = input('Do you wan to play again? Press any key to play again, press q/Q to exit.')
        if continue_game.lower() == 'q':
            break