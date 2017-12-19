"""

#Milestone Project 2 - Blackjack Game In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the players total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:

You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
Feel free to expand this game-try including multiple players. Try adding in Double-Down and card splits! Remember to you are free to use any resources you want and as always:

"""

# import libs
import random

class TheDeck(object):

    def __init__(self):
        self.suits = 'cdhs'
        self.vals = '23456789TJQKA'
        self.deck = []
        self.this_card = ''

        for s in self.suits:
            for v in self.vals:
                this_card = s + v
                self.deck.append(this_card)

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def printDeck(self):
        print(self.deck)

    def drawCard(self):
        card_num = random.randint(1,52)
        drawn_card = self.deck[card_num]
        del self.deck[card_num]
        return drawn_card

    def evalCard(self,card):
        card_points = 0
        suit = ''
        if card[0] == 'c':
            suit = 'Clubs'
        elif card[0] == 'd':
            suit = 'Diamonds'
        elif card[0] == 'h':
            suit = 'Hearts'
        else:
            suit = 'Spades'

        if card[1] == 'T':
            card_val = "Ten"
            points = 10
        elif card[1] == 'J':
            card_val = "Jack"
            points = 10
        elif card[1] == 'Q':
            card_val = "Queen"
            points = 10
        elif card[1] == 'K':
            card_val = "King"
            points = 10
        elif card[1] == 'A':
            points = 10
            card_val = "Ace"
        else:
            card_val = card[1]
            points = int(card[1])

        print(points)
        return 'You drew the ' + card_val + ' of ' + suit
