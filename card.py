# Poker
from loguru import logger


class Card():
    def __init__(self, color: str=None, number: int=None, status: str=None) -> None:
        self.color = color
        self.number = number
        self.status = None
        self.color_list = ["Diamonds", "Hearts", "Spades", "Clubs"]
        self.check()

    @logger.catch
    def check(self):
        if self.status not in [None, "Red Joker", "Black Joker"]:
            logger.error(f"Card do not exist!")
        if not self.status:
            if self.number not in list(range(1,14)):
                logger.error(f"Card do not exist!")
            elif self.color not in self.color_list:
                logger.error(f"Card do not exist!")


if __name__ == "__main__":
    D6 = Card("Diamonds", 45)