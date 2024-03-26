import csv
from typing import List

from TruthFalse.game_status import GameStatus
from TruthFalse.invalid_operation_exception import InvalidOperationException


class Game:

    def __init__(self, filename: str = 'data/Questions.csv', max_tries: int = 3):
        if max_tries > 5:
            raise ValueError('Max tries must be less than 5!')

        self.__filename = filename
        self.__max_tries = max_tries
        self._counter = 0
        self._misses = 0
        self.__game_status = GameStatus.NOT_STARTED
        self.__questions = []
        with open(self.__filename, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            self.__questions = [row for row in reader]

        self.__answered_indexes = [False for _ in range(len(self.__questions))]

    def start_game(self):
        self.__game_status = GameStatus.IN_PROGRESS

    @property
    def question(self):
        if not self.answered_indexes[self.counter]:
            return self.questions[self.counter][0]

    @property
    def answer_description(self):
        return self.__questions[self.counter][2]

    def get_answer(self, answer: str) -> List[bool]:
        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationException(f'Game status: {self.game_status}')

        if self.misses > self.max_tries:
            raise InvalidOperationException(f'Exceeded max tries: {self.max_tries}')

        if not self.answered_indexes[self.counter]:
            question = self.questions[self.counter]
            correct_answer = question[1]

            if answer.lower() == correct_answer[0].lower():
                self.__answered_indexes[self.counter] = True
                self._counter += 1
            elif answer == 'next':
                self._counter += 1
            else:
                self._counter += 1
                self._misses += 1

        if self._counter == len(self.questions):
            self.__game_status = GameStatus.WON
        elif self.misses == self.max_tries:
            self.__game_status = GameStatus.LOST

        return self.answered_indexes

    @property
    def get_game_status(self):
        return self.__game_status

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def max_tries(self) -> int:
        return self.__max_tries

    @property
    def counter(self) -> int:
        return self._counter

    @property
    def misses(self) -> int:
        return self._misses

    @property
    def questions(self) -> list[list[str]]:
        return self.__questions

    @property
    def answered_indexes(self) -> List:
        return self.__answered_indexes


