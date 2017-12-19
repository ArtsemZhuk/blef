from random import shuffle, seed
from hashlib import sha256

# shift = int(sha256(l1.encode("utf8")).hexdigest(), 16)

def get_cards():
    cards = []
    for i in list("23456789ВДКТ") + ["10"]:
        for j in ["пик", "треф", "червей", "бубен"]:
            cards += [i+" "+j]
    return cards


def get_hand(me, ratio, hsh):
    cards = get_cards()
    seed(hsh + sum(ratio))
    shuffle(cards)

    deck = []
    my = []
    for i in range(len(ratio)):
        for t in range(ratio[i]):
            x, cards = cards[0], cards[1:]
            deck += [x]
            if i == me:
                my += [x]
    return sorted(my)


def get_all(ratio, hsh):
    cards = get_cards()
    seed(hsh + sum(ratio))
    shuffle(cards)

    deck = []
    for i in range(len(ratio)):
        for t in range(ratio[i]):
            x, cards = cards[0], cards[1:]
            deck += [x]
    return sorted(deck)


if __name__ == '__main__':
    ratio = [1, 2, 3]
    hsh = 123
    for me in range(0, 3):
        print(get_hand(me, ratio, hsh))
    print(get_all(ratio, hsh))
