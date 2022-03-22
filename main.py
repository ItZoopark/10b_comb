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