import random

class RockPaperScissor:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choices}): ')
        if user_choice.lower() in self.choices:
            return user_choice 
        print(f'Invalid choice. You must select from {self.choices}')
        return self.get_player_choice() # recursive method

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"

        win_combinations =[('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'rock')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                return "Congratulations! You won!"

            return "Oh no! You lost!"

    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"Computer's choice: {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':
    game = RockPaperScissor('Sahar')

    while True:
        game.play()

        continue_game = input('Do you wan to play again? Press any key to play again, press q/Q to exit.')
        if continue_game.lower() == 'q':
            break