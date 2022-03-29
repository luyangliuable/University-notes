def char_to_dec(character: str) -> int:
    lowest_dec = 97
    dec = ord(character) - lowest_dec
    return dec

def count(word: str) -> list[int]:
    letters_in_alphabet = 26
    counter = [0]*letters_in_alphabet
    # Normal the ascii from 97 since at this number it is when "a" starts
    for i in range(len(word)):
        dec = char_to_dec(word[i])
        # print("for char:", word[i], "you get", dec)
        counter[dec] += 1

    return counter


def count_sort(input_list: list[str], index_to_sort: int) -> list[str]:
    count = [0]*26
    pos = [0]*26

    for i in range(len(input_list)):
        dec = char_to_dec(input_list[i][index_to_sort])
        count[dec] += 1

    for i in range(26):
        pos[i] = pos[i-1] + count[i-1]

    temp = [""]*(len(input_list))
    for i in range(len(input_list)):
        dec = char_to_dec(input_list[i][index_to_sort])
        temp[pos[dec]] = input_list[i]
        pos[dec] += 1

    return temp


def trainer(wordlist: list[str], word: str, marker: list[int]) -> list[str]:
    orginal = wordlist
    res = []
    tmp = ""
    for i in range(len(marker)):
        j = len(marker) - i - 1
        if marker[j] == 0:
            wordlist = count_sort(wordlist, j)
            tmp = word[j] + tmp

    for j in range(len(wordlist)):
        contain_same_letters = True
        for i in range(len(word)):
            if  marker[i] == 0 and wordlist[j][i] == word[i]:
                contain_same_letters = False
                # print("not in word", wordlist[j])
                break
            elif marker[i] == 1 and wordlist[j][i] != word[i]:
                contain_same_letters = False
                # print("not in position", wordlist[j])
                break

        if contain_same_letters:
            res.append(wordlist[j])

    return res


wordlist = ['costar', 'carets', 'recast', 'traces', 'reacts', 'caster', 'caters', 'crates', 'actors', 'castor']
# wordlist = ['aaaaaa', 'bbbbbb', 'cccccc']

word = 'catrse'
marker = [1,1,0,0,0,0]
res = trainer(wordlist, word, marker)

print(res)
for i in range(len(res)):
    res[i] = res[i][2:]

# print(res)

# print(trainer(wordlist, word, marker))

# print(count("aabbccz"))
