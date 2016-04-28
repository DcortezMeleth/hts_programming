from itertools import permutations

result = ''
with open('entrywordlist.txt') as entries_file:
    for line in entries_file:
        permutation_list = [''.join(p) for p in permutations(line.strip())]
        with open('wordlist.txt') as wordlist_file:
            for line2 in wordlist_file:
                word = line2.strip()
                if word in permutation_list:
                    result += word
                    result += ','
                    break
print result[:-1]