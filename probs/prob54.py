"""Problem ?: ???"""
import unittest

hand_types = {
    (1, 1, 1, 1, 1): "high_card",
    (2, 1, 1, 1): "pair",
    (2, 2, 1): "two_pair",
    (3, 1, 1): "three_of_a_kind",
    (3, 2): "full_house",
    (4, 1): "four_of_a_kind"
}

hand_scores = {
    "high_card": 0,
    "pair": 1,
    "two_pair": 2,
    "three_of_a_kind": 3,
    "straight": 4,
    "flush": 5,
    "full_house": 6,
    "four_of_a_kind": 7,
    "straight_flush": 8,
    "royal_flush": 9,
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
    hand_summary = {"type": None, "cards": []}
    hand.sort(key = lambda card: -card_vals[card[0]])
    flush = (len(set([card[1] for card in hand])) == 1)
    straight = ([card_vals[card[0]] for card in hand[::-1]] ==
                list(range(card_vals[hand[-1][0]], card_vals[hand[0][0]]+1)))
    if not straight:
        if [card_vals[card[0]] for card in hand[::-1]] == [1, 2, 3, 4, 14]:
            straight = True
    if straight and flush:
        if hand[0][0] == "A":
            hand_summary["type"] = "royal_flush"
            hand_summary["cards"] = hand
        else:
            hand_summary["type"] = "straight_flush"
            hand_summary["cards"] = hand
        return hand_summary
    if flush:
        hand_summary["type"] = "flush"
        hand_summary["cards"] = hand
        return hand_summary
    if straight:
        hand_summary["type"] = "straight"
        hand_summary["cards"] = hand
        return hand_summary
    hand_table = {}
    for card in hand:
        if card[0] in hand_table:
            hand_table[card[0]].append(card)
        else:
            hand_table[card[0]] = [card]
    pairs = list(hand_table.items())
    pairs.sort(key = lambda x: -len(x[1]))
    hand_summary["type"] = hand_types[tuple(len(p[1]) for p in pairs)]
    cards = [pairs[0][1]]
    for pair in pairs[1:]:
        if len(pair[1]) == len(cards[-1]):
            i = 0
            while i < len(cards) and (len(pair[1]) < len(cards[i]) or card_vals[pair[1][0][0]] < card_vals[cards[i][0][0]]):
                i += 1
            cards.insert(i, pair[1])
        else:
            cards.append(pair[1])
    hand_summary["cards"] = [c for lst in cards for c in lst]
    return hand_summary

def find_winner(hand1, hand2):
    hand1_summary = find_hand(hand1)
    hand2_summary = find_hand(hand2)
    if hand_scores[hand1_summary["type"]] != hand_scores[hand2_summary["type"]]:
        return 1 if hand_scores[hand1_summary["type"]] > hand_scores[hand2_summary["type"]] else 2
    i = 0
    while card_vals[hand1_summary["cards"][i][0]] == card_vals[hand2_summary["cards"][i][0]]:
        i += 1
    return 1 if card_vals[hand1_summary["cards"][i][0]] > card_vals[hand2_summary["cards"][i][0]] else 2

def solution():
    p1_score = 0
    hands1, hands2 = load_hands("inputs/prob54.txt")
    for hand1, hand2 in zip(hands1, hands2):
        winner = find_winner(hand1, hand2)
        if winner == 1:
            p1_score += 1
    return p1_score

class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
