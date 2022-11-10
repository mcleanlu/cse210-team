"""
hilo.py

Authors: Luke McLean, Carter Kearns
Assignment: Week 1 Teach
"""

import random

# Alternatively to having one "Card()" control two random values, create two "Card()"s and give them a "is_higher(self, other_card)" method.
class Card:
    def __init__(self):
        self.value = None
        self.next_value = None

    def draw(self):
        """Randomly choose the values for both card"""
        self.value = random.randint(1, 13)
        self.next_value = random.randint(1, 13)

    def was_higher(self):
        """Return True if the second card is higher"""
        return self.next_value >= self.value

    def was_lower(self):
        """Return True if the second card is lower"""
        return self.next_value < self.value


SCORE_TABLE = {True: 100, False: -75}


class Director:
    def __init__(self):
        self.score = 300
        self.card = Card()

    def play(self):
        want_to_play = "y"
        while want_to_play.lower() == "y" or want_to_play == "":
            self.do_turn()
            print(f"Your score is: {self.score}")

            if self.score <= 0:
                print("Game over!")
                break

            want_to_play = input("Play again? [Y/n] ").strip()
            print()

    def do_turn(self):
        self.card.draw()
        print(f"The card is: {self.card.value}")
        guessed_higher = self.ask_higher()
        print(f"The next card was: {self.card.next_value}")

        was_correct = False
        if (guessed_higher and self.card.was_higher()) or (
            (not guessed_higher) and self.card.was_lower()
        ):
            was_correct = True

        self.score += SCORE_TABLE[was_correct]

    def ask_higher(self):
        """Return True if the user thinks the next card will be higher, False otherwise"""
        return input("Higher or lower? [h/l] ").lower() == "h"


def main():
    Director().play()


if __name__ == "__main__":
    main()
