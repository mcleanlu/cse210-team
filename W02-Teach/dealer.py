from card import Card


class Dealer:
    """
    Dealer class, controls the process of the game
    """

    def __init__(self, player):
        """
        The player starts off with the following values
        """
        self.card = Card()
        self.card1_value = 0
        self.card2_value = 0
        self.hilo_choice = ""
        self.player = player

    def choice(self):
        """
        Player chooses whether the card is hi or low
        """
        self.hilo_choice = input("Higher or Lower? [h/l] ")
        return (self.hilo_choice)

    def playerScore(self):
        """
        If the player is correct in guessing, then they are assigned a win, otherwise they lose
        """
        if (self.card1_value < self.card2_value and self.hilo_choice == "h"):
            self.player.win()
        elif (self.card1_value > self.card2_value and self.hilo_choice == "l"):
            self.player.win()
        else:
            self.player.lose()

    def gameCycle(self):

        another_round = "y"
        while (another_round == "y"):

            # deal 1
            self.card1_value = self.card.card_number()
            print("The card is {}".format(self.card1_value))

            # player choice
            self.hilo_choice = self.choice()

            # deal 2
            self.card2_value = self.card.card_number()
            print("The next card was {}".format(self.card2_value))

            # print the score
            self.hilo_choice = self.playerScore()
            print("Your score is: ", self.player.total_score())

            if (self.player.total_score() > 0):
                another_round = input("Play again? [y/n] ")
            else:
                another_round = "n"
