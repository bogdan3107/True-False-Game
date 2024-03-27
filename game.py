from typing import Callable, List

from TruthFalse.game_result import GameResult
from TruthFalse.game_status import GameStatus
from TruthFalse.question import Question


class Game:

    def __init__(self, file_path: str, end_of_game_event: Callable, allowed_mistakes: int):
        self.__file_path = file_path
        self.__allowed_mistakes = allowed_mistakes
        self.__end_of_game_event = end_of_game_event
        self.__mistakes = 0
        self.__questions: List[Question] = []
        self.__counter = 0
        self.__game_status = GameStatus.IN_PROGRESS

        self.__fill_in_question(file_path, self.__questions)

    def get_next_question(self) -> Question:
        return self.__questions[self.__counter]

    def give_answer(self, answer: bool):
        def is_last_question():
            return self.__counter == len(self.__questions) - 1

        def exceeded_allowed_mistakes():
            return self.__mistakes > self.__allowed_mistakes

        if self.__questions[self.__counter].is_true != answer:
            self.__mistakes += 1

        if is_last_question() or exceeded_allowed_mistakes():
            self.__game_status = GameStatus.GAME_IS_OVER

            result = GameResult(self.__counter, self.__mistakes, self.__mistakes <= self.__allowed_mistakes)
            self.__end_of_game_event(result)

        self.__counter += 1

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    def __fill_in_question(self, file_path, questions):
        with open(file_path, encoding='utf8') as f:
            for line in f:
                q = self.__parse_line(line)
                questions.append(q)

    def __parse_line(self, line) -> Question:
        parts = line.split(';')
        text = parts[0]
        is_correct = parts[1] == 'Yes'
        explanation = parts[2]

        return Question(text, is_correct, explanation)



