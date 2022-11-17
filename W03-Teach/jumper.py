class Jumper:
    def __init__(self):
        self.strings_left = 5

    def guess_incorrect(self):
        self.strings_left -= 1
