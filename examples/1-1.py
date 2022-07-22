from collections import namedtuple


Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank=rank, suit=suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


def spades_high(_card: Card):
    suit_values = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}
    rank_values = FrenchDeck.ranks.index(_card.rank)
    return rank_values * len(suit_values) + suit_values[_card.suit]


if __name__ == '__main__':
    from random import choice

    beer_card = Card(rank=7, suit='diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))

    print(deck[0])
    print(deck[1])

    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    print(deck[:3])
    print(deck[12::13])

    for card in deck:
        print(card)

    for card in reversed(deck):
        print(card)

    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)

    for card in sorted(deck, key=spades_high):
        print(card)
