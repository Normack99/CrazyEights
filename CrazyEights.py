import DeckOfCards as d
import os

class CrazyEights:
    def __init__(self):
        self.deck = d.Deck()
        self.hands = []
        players = int(input("How many players are there? "))
        for player in range(players):
            name = input(f"What is the name of player {player + 1}: ")
            self.hands.append(d.Hand(name, 5, self.deck))
        while True:
            self.topstack = self.deck.draw()
            if self.topstack.name == "8":
                self.deck.shuffle_card_into_deck(self.topstack)
            else:
                self.deck.graveyard.append(self.topstack)
                break
    
    def turn(self, player: int):
        while True:
            self.input(player)
            if self.cardname != "pass" and self.cardsuit != "pass":
                self.presentcard = d.Card(self.cardname, self.cardsuit)  
                if self.hands[player].validcard(self.presentcard) == True:
                    if self.validcard(self.presentcard) == True:
                        self.topstack = self.hands[player].play_card(self.presentcard)
                        if self.topstack.name == "8":
                            self.eightlogic()
                        break
                    else:
                        print()
                        if self.topstack.name != "8":
                            print("You cannot play this card. You must play a card that matches a suit or rank with the top card")
                        else:
                            print("You cannot play this card. You must play a card that matches the specified suit")
                        anykey()
                else:
                    print()
                    print("That card is not in your hand")
                    anykey()
            elif self.cardname == "pass" or self.cardsuit == "pass":
                drawn_card = self.hands[player].draw()
                print()
                print(f"You have drawn the {str(drawn_card)}")
                break
            if len(self.deck) == 0:
                print()
                print("Shuffling discard pile back into deck")
                self.deck.shuffle_graveyard_into_deck()

    def input(self, player: int):
        if self.topstack.name == "8":
            print(f"You must play a card of the suit: {self.suit}")
        else:
            print(f"The card on top is the {str(self.topstack)}")
        print()
        print(f"{self.hands[player].name} Handsize: {len(self.hands[player])}\n{self.hands[player]}")
        print("What card would you like to play? Either input a card or pass")
        self.cardname = input("Rank: ")
        self.cardsuit = input("Suit: ")

    def eightlogic(self):
        print()
        self.suit = ""
        while self.suit not in d.suits:
            self.suit = input("Which suit does the next player have to play: ")

    def validcard(self, card: d.Card) -> bool:
        if self.topstack.name == "8" and card.suit == self.suit:
            return True
        elif self.topstack.name != "8" and card.suit == self.topstack.suit or card.name == self.topstack.name or card.name == "8":
            return True
        else:
            return False

def anykey():
    print()
    input("Press any key to continue: ")
    os.system("cls")

def gameloop():
    win = False
    while win == False:
        for player in range(len(game.hands)):
            game.turn(player)
            anykey()
            if len(game.hands[player]) == 0:
                print(f"{game.hands[player].name} has won the game")
                win = True
    anykey()
    quit()

if __name__ == "__main__":
    os.system("cls")
    game = CrazyEights()
    anykey()
    gameloop()