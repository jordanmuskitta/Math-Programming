import numpy as np
from dataclasses import dataclass, field
from typing import Tuple, List


@dataclass
class Player:
    hand: Tuple = field(default_factory=tuple)

    def calc_prob(self): 
        pass


@dataclass
class Dealer: 
    deck: np.ndarray
    n_players: int
    players: List[Player] = field(default_factory=list)

    def __post_init__(self):
        self.players = [Player() for _ in range(self.n_players)]

    def deal(self, n_cards=2):
        avail_cards = list(self.deck)
        for player in self.players: 
            dealt_hand_list = []
            for i in range(n_cards):
                if avail_cards: 
                    dealt_hand = np.random.choice(avail_cards)
                    dealt_hand_list.append(dealt_hand)
                    avail_cards.remove(dealt_hand)
            player.hand = tuple(dealt_hand_list)

        self.deck = np.array(avail_cards)

    def deal_flop(self): 
        avail_cards = list(self.deck)
        flop = []
        for _ in range(3): 
            if avail_cards: 
                dealt_card = np.random.choice(avail_cards)
                flop.append(dealt_card)
                avail_cards.remove(dealt_card)

        self.flop = flop
        self.deck = np.array(avail_cards)

if __name__ == "__main__":
    
    deck = np.array([
    # Spades
    '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
    # Clubs
    '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
    # Hearts
    '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
    # Diamonds
    '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦'
    ])
    
    # Instantiate dealer class with the number of players
    dealer = Dealer(deck=deck, n_players=3)

    # Call the deal method
    dealer.deal()
    
    # Show each players hand
    for idx, val in enumerate(dealer.players):
        print(f"Player {idx}: {val.hand}")

    # Dealer deals the flop
    dealer.deal_flop()

    # Output the remaining cards and the flop
    print(f"\nThe flop: {dealer.flop}")
    print(f"\nRemaining deck: {dealer.deck}")
