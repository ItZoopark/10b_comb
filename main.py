import itertools


# print(list(itertools.product('СОЛ', repeat=2)))
# print(list(itertools.permutations('СОЛ')))
def pol_3223():
    count = 0
    for x in itertools.product('СОЛВЕЙ', repeat=6):
        word = ''.join(x)
        if word.count('Й') <= 1 and word[0] != 'Й' and word[-1] != 'Й':
            if 'ЕЙ' not in word and 'ЙЕ' not in word:
                count += 1
    print(count)


def pol_4199():
    count = 0
    glas = 'ЕИЯ'
    sogl = 'КСН'
    for r in range(3, 8):
        for x in itertools.product('КСЕНИЯ', repeat=r):
            word = ''.join(x)
            if word.count('Е') <= 2 and word.count('И') <= 2 and word.count('Я') <= 2:
                if ((word[0] in sogl) and len(set(word) & set(sogl)) == 1) or \
                        len(set(word) & set(sogl)) == 0:
                    count += 1
    print(count)


pol_4199()
