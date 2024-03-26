from TruthFalse.game import Game
from TruthFalse.game_status import GameStatus

game = Game()
game.start_game()

print("Welcome to TruthFalse! You can answer Y for yes or N for no. You can skip the question "
      "by typing \"next\" \n or \"status \" to see the status of the game")

while game.game_status == GameStatus.IN_PROGRESS:
    print(f'\n\n\nQuestions list {game.answered_indexes}. It become True if answered correct.')
    print(f'Tries left: {game.max_tries - game.misses}')
    print(f'Your question is: {game.question}')

    answer = input('Please neter your answer.\n')
    if answer == 'status':
        print(game.game_status)

    game.get_answer(answer)
    print(game.answer_description)

if game.game_status == GameStatus.WON:
    print('Congratulations! You won the game')

if game.game_status == GameStatus.LOST:
    print('Sorry! Try again')
