import sys
from collections import defaultdict


def solution(cards):
    card_dic = defaultdict(list)
    cnt = [13, 13, 13, 13]

    for card in cards:
        if card[0] == 'P':
            if card in card_dic['P']:
                return "GRESKA"
            else:
                card_dic['P'].append(card)
                cnt[0] -= 1
        elif card[0] == 'K':
            if card in card_dic['K']:
                return "GRESKA"
            else:
                card_dic['K'].append(card)
                cnt[1] -= 1

        elif card[0] == 'H':
            if card in card_dic['H']:
                return "GRESKA"
            else:
                card_dic['H'].append(card)
                cnt[2] -= 1

        else:
            if card in card_dic['T']:
                return "GRESKA"
            else:
                card_dic['T'].append(card)
                cnt[3] -= 1

    return " ".join(map(str, cnt))


s = sys.stdin.readline()

card_list = [s[i:i + 3] for i in range(0, len(s), 3)]
card_list.pop()

print(solution(card_list))
