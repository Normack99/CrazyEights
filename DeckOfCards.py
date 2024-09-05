import random
from functools import total_ordering

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]

@total_ordering
class Card:
    def __init__(self, name: str, suit: str):
        self.name = name
        self.suit = suit
        self.value = ranks.index(self.name)

    def __str__(self) -> str:
        return f"{self.name} of {self.suit}"

    def __lt__(self, other) -> bool:
        card = self.value
        othercard = other.value
        return card < othercard

    def __gt__(self, other) -> bool:
        card = self.value
        othercard = other.value
        return card > othercard

    def __eq__(self, other) -> bool:
        card = self.suit, self.name
        othercard = other.suit, other.name
        return card == othercard

class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
        self.graveyard = []
        random.shuffle(self.deck)

    def draw(self) -> Card:
        return self.deck.pop(0)

    def shuffle_graveyard_into_deck(self):
        self.deck.extend(self.graveyard)
        self.graveyard.clear()
        random.shuffle(self.deck)

    def shuffle_card_into_deck(self, card: Card):
        self.deck.insert(random.randint(0, len(self.deck) - 1), card)
        self.graveyard.remove(card)

    def __str__(self) -> str:
        string = ""
        for card in self.deck:
            string += f"{str(card)}\n"
        return string

class Hand:
    def __init__(self, name, handsize: int, deck: Deck):
        self.name = name
        self.hand = []
        self.deck = deck
        for cards in range(handsize):
            self.draw() 

    def draw(self) -> Card:
        self.hand.append(self.deck.draw())
        return self.hand[-1]

    def play_card(self, card: Card) -> Card:
        self.hand.pop(self.hand.index(card))
        self.deck.graveyard.append(card)
        return card

    def validcard(self, card: Card) -> bool:
        if card in self.hand:
            return True
    
    def __str__(self) -> str:
        string = ""
        for card in self.hand:
            string += f"{str(card)}\n"
        return string

    def __len__(self) -> int:
        return len(self.hand)