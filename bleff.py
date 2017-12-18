from random import shuffle, seed
from hashlib import sha256

cards = []
for i in list("23456789ВДКТ") + ["10"]:
    for j in ["пик", "треф", "червей", "бубен"]:
        cards += [i+" "+j]

f = open("input.txt")

l1 = f.readline().strip()
l2 = f.readline().strip()

shift = int(sha256(l1.encode("utf8")).hexdigest(), 16)

seed(l1 + l2)
ratio = list(map(int, l2.split()))
print("move: {}".format((sum(ratio) + shift) % len(ratio)))
print()
me = int(f.readline())

shuffle(cards)

cards2 = [x for x in cards]

deck = []
my = []
for i in range(len(ratio)):
    for t in range(ratio[i]):
        x, cards2 = cards2[0], cards2[1:]
        deck += [x]
        if i == me:
            my += [x]
print("\n".join(sorted(my)))
print()

while input() != 'q':
    pass
print("\n".join(sorted(deck)))
