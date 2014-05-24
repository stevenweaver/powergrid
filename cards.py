class Card:
    def __init__(self, min_bid, num_resource, resource_type, ppp):
        self.min_bid = min_bid
        self.num_resource = num_resource
        self.resource_type = resource_type
        self.ppp = ppp

class Deck:
''' Class to hold card deck. Used for functions like draw_random, etc'''
    def load_cards(self):
        cards = []
        cards.append(Card(3,  2,   'O',   1))
        cards.append(Card(4,  2,   'C',   1))
        cards.append(Card(5,  2,   'H',   1))
        cards.append(Card(6,  1,   'T',   1))
        cards.append(Card(7,  3,   'O',   2))
        cards.append(Card(8,  3,   'C',   2))
        cards.append(Card(9,  1,   'O',   1))
        cards.append(Card(10,  2,   'C',   2))
        cards.append(Card(11,  1,   'U',   2))
        cards.append(Card(12,  2,   'H',   2))
        cards.append(Card(13,  0,   'E',   1))
        cards.append(Card(14,  2,   'T',   2))
        cards.append(Card(15,  2,   'C',   3))
        cards.append(Card(16,  2,   'O',   3))
        cards.append(Card(17,  1,   'U',   2))
        cards.append(Card(18,  0,   'E',   2))
        cards.append(Card(19,  2,   'T',   3))
        cards.append(Card(20,  3,   'C',   5))
        cards.append(Card(21,  2,   'H',   4))
        cards.append(Card(22,  0,   'E',   2))
        cards.append(Card(23,  1,   'U',   3))
        cards.append(Card(24,  2,   'T',   4))
        cards.append(Card(25,  2,   'C',   5))
        cards.append(Card(26,  2,   'O',   5))
        cards.append(Card(27,  0,   'E',   3))
        cards.append(Card(28,  1,   'U',   4))
        cards.append(Card(29,  1,   'H',   4))
        cards.append(Card(30,  3,   'G',   6))
        cards.append(Card(31,  3,   'C',   6))
        cards.append(Card(32,  3,   0,   6))
        cards.append(Card(33,  0,   'E',   4))
        cards.append(Card(34,  1,   'U',   5))
        cards.append(Card(35,  1,   'O',   5))
        cards.append(Card(36,  3,   'C',   7))
        cards.append(Card(37,  0,   'E',   4))
        cards.append(Card(38,  3,   'T',   7))
        cards.append(Card(39,  1,   'U',   6))
        cards.append(Card(40,  2,   'O',   6))
        cards.append(Card(42,  2,   'C',   6))
        cards.append(Card(44,  0,   'E',   5))
        cards.append(Card(46,  3,   'H',   7))
        cards.append(Card(50,  0,   'E',   6))
        return cards

    def __init__(self):
        self.cards = self.load_cards()

