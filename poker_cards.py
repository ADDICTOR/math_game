# Poker cards
from loguru import logger
from card import Card


class Deck():
    def __init__(self) -> None:
        self.color_list = ["Diamonds", "Hearts", "Spades", "Clubs"]
        self.deck = []
        self.init()

    def init(self):
        for color in self.color_list:
            for num in range(1,14):
                card = Card(color=color, number=num)
                self.deck.append(card)
        RJoker = card(status="RJoker")
        BJoker = card(status="BJoker")
        self.deck.append(RJoker, BJoker)