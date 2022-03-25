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


# pol_4199()
def pol_4198():
    sogl = 'КРШ'
    count = 0
    for r in range(3, 6):
        for i in itertools.product('КРЫША', repeat=r):
            word = ''.join(i)
            if word.count('Ы') <= 2 and word.count('А') <= 2 \
                    and word.count('К') <= 1 and word.count('Р') <= 1 and word.count('Ш') <= 1:
                if len(set(word) & set(sogl)) == 1 and word[0] in sogl or \
                        len(set(word) & set(sogl)) == 0:
                    print(word)
                    count += 1
    print(count)


# pol_4198()
# ДЗ ---------------------------------------
def pol_1901():
    alpha16 = '0123456789ABCDEF'
    evens = '02468'
    odds = '13579'
    count = 0
    for i in itertools.product(alpha16, repeat=3):
        word = ''.join(i)
        if len(set(word)) == len(word):
            if word[0] != '0' and (word[0] in evens and word[1] in odds and word[2] in evens or \
                                   word[0] in odds and word[1] in evens and word[2] in odds):
                print(word)
                count += 1
    print(count)


pol_1901()
