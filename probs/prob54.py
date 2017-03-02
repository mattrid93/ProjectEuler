"""Problem ?: ???"""
import unittest

hand_scores = {
    "high_card": 0,
    "pair": 1,
    "two_pair": 2,
    "three_of_a_kind": 3,
    "straight": 4,
    "flush": 5,
    "four_of_a_kind": 6,
    "straight_flush": 7,
    "royal_flush": 8,
}

card_vals = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

def load_hands(filename):
    with open(filename) as f:
        p1, p2 = [], []
        for line in f.readlines():
            p1.append(line.split()[:5])
            p2.append(line.split()[5:])
        return p1, p2

def find_hand(hand):
    hand_summary = {"type": None, "hand_cards": [], "other_cards": []}
    hand.sort(key = lambda card: -card_vals[card[0]])
    flush = (len(set([card[1] for card in hand])) == 1)
    straight = ([card_vals[card[0]] for card in hand[::-1]] ==
                list(range(card_vals[hand[0][0]], card_vals[hand[-1][0]]+1)))
    if not straight:
        if [card_vals[card[0]] for card in hand[::-1]] == [1, 2, 3, 4, 14]:
            straight = True
    if straight and flush:
        if hand[0][0] == "A":
            hand_summary["type"] = "royal_flush"
            hand_summary["hand_cards"] = hand
        else:
            hand_summary["type"] = "straight_flush"
            hand_summary["hand_cards"] = hand
        return hand_summary
    if flush:
        hand_summary["type"] = "flush"
        hand_summary["hand_cards"] = hand
        return hand_summary
    if straight:
        hand_summary["type"] = "straight"
        hand_summary["hand_cards"] = hand
        return hand_summary
    hand_table = {}
    for card in hand:
        if card[0] in hand_table:
            hand_table[card[0]].append(card)
        else:
            hand_table[card[0]] = [card]
    if len(hand_table) == 2:
        pass

def find_winner(hand1, hand2):
    hand1_score = find_hand(hand1)
    hand2_score = find_hand(hand2)

def solution():
    hands1, hands2 = load_hands("inputs/prob54_test.txt")
    for hand1, hand2 in zip(hands1, hands2):
        find_winner(hand1, hand2)

class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
