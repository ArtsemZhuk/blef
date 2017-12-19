from random import shuffle, seed, randint
from hashlib import sha256
from copy import copy

def get_cards():
    cards = []
    for i in list("23456789ВДКТ") + ["10"]:
        for j in ["пик", "треф", "червей", "бубен"]:
            cards += [i+" "+j]
    return cards


class State:

    def __init__(self, ratio):
        self.hsh = randint(0, 2 ** 32 - 1)
        self.ratio = ratio

    def get_deck(self):
        seed(self.hsh)
        deck = get_cards()
        shuffle(deck)
        return deck

    def get_hand(self, me):
        l = sum(ratio[:me])
        r = sum(ratio[:me + 1])
        deck = self.get_deck()
        return sorted(deck[l:r])

    def get_table(self):
        deck = self.get_deck()
        table = deck[:sum(self.ratio)]
        return table
        

if __name__ == '__main__':
    ratio = [1, 2, 3]
    s = State(ratio)
    for me in range(0, 3):
        print(s.get_hand(me))
    print(s.get_table())
