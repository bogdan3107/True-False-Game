from TruthFalse.game import Game
from TruthFalse.game_result import GameResult
from TruthFalse.game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f"Questions passed: {result.questions_passed}. Mistakes made: {result.mistakes_made}.")
    print(f"You won" if result.won else "You lost")


game = Game("data/Questions.csv", end_of_game_handler, allowed_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:
    q = game.get_next_question()
    print("Please answer 'y' or 'n' to the following question: ")

    print(q.text)

    answer = input() == "y"

    if q.is_true == answer:
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"Here is why: {q.explanation}")

    game.give_answer(answer)


