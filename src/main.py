from src.game_logic import RockPaperScissor

user_name = input('Enter your name: ')
game = RockPaperScissor(user_name)

if __name__ == '__main__':
    while True:
        game.play()

        continue_game = input('Do you wan to play again? Press any key to play again, press q/Q to exit.')
        if continue_game.lower() == 'q':
            break
    