from enum import Enum
import random
import time

class DifficultyLevel(Enum):
    EASY = 8
    MEDIUM = 6
    HARD = 4

class Difficulty:
    @staticmethod
    def get_chances(level: DifficultyLevel) -> int:
        return level.value

class PlayerInterface:
    @staticmethod
    def get_difficulty():
        print("Choose difficulty:\n1. Easy\n2. Medium\n3. Hard")
        options = {"1": DifficultyLevel.EASY, "2": DifficultyLevel.MEDIUM, "3": DifficultyLevel.HARD}
        while True:
            choice = input("Your choice: ")
            if choice in options:
                return options[choice]
            print("Invalid choice.")

    @staticmethod
    def get_guess() -> int:
        while True:
            try:
                return int(input("Enter your guess: "))
            except ValueError:
                print("Invalid number. Try again.")

    @staticmethod
    def ask_play_again() -> bool:
        return input("Play again? (Y/N): ").strip().upper() == 'Y'

    @staticmethod
    def show_message(msg: str):
        print(msg)

class HintSystem:
    @staticmethod
    def provide_hint(guess_history, target):
        if len(guess_history) >= 2 and guess_history[-1] == guess_history[-2]:
            parity = 'even' if target % 2 == 0 else 'odd'
            return f"Hint: The number is {parity}."
        return None

class Round:
    def __init__(self, difficulty: DifficultyLevel):
        self.target = random.randint(1, 100)
        self.chances = Difficulty.get_chances(difficulty)
        self.guesses = []
        self.start_time = None
        self.end_time = None

    def play(self, interface: PlayerInterface):
        self.start_time = time.time()
        for attempt in range(1, self.chances + 1):
            guess = interface.get_guess()
            self.guesses.append(guess)

            if hint := HintSystem.provide_hint(self.guesses, self.target):
                interface.show_message(hint)

            if guess == self.target:
                self.end_time = time.time()
                duration = self.end_time - self.start_time
                interface.show_message(f"🎉 Correct! Attempts: {attempt}, Time: {duration:.2f}s")
                return {"result": "win", "attempts": attempt, "time": duration}

            elif guess < self.target:
                interface.show_message("The number is higher.")
            else:
                interface.show_message("The number is lower.")

        self.end_time = time.time()
        interface.show_message(f"❌ You lost! The number was {self.target}. Time: {self.end_time - self.start_time:.2f}s")
        return {"result": "lose", "target": self.target, "time": self.end_time - self.start_time}

class GameEngine:
    def __init__(self):
        self.interface = PlayerInterface()

    def start(self):
        self.interface.show_message("🎯 Welcome to the Number Guessing Game!")
        while True:
            difficulty = self.interface.get_difficulty()
            game_round = Round(difficulty)
            game_round.play(self.interface)

            if not self.interface.ask_play_again():
                self.interface.show_message("👋 Thanks for playing!")
                break


a = GameEngine()
a.start()