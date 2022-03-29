def char_to_dec(character: str) -> int:
    """
    This function converts a character from [a-z] and turns it into an int that starts with 0 for a and 25 for z

        Parameters:
        Character (str): A string with length of 1 that should be in the range of [a-z]

        Returns:
        An int that corresponds to the index of [a-z] if character satisfy post condition


        Time Complexity:
            Worse case: O(1)

        Space complexity:
            Worse case: O(1)
    """


    if len(character) > 1 or len(character) == 0:
        raise Exception("The input character must be of length 1")

    lowest_dec = 97
    dec = ord(character) - lowest_dec
    # assert dec > 0 and dec <= 25, "the input character must be between [a-z]"
    # TODO fix assertion
    return dec

def count(word: str) -> list[int]:
    """
    This function counts every letter in a word and translates each letter into an increment on the counter.

        Parameters:
            word (str): A string that require each of its letter to be counted

        Returns:
            A list of int that contains the counter that goes from a to z contained in the alphabet

        Time Complexity:
            Worst case: O(M)
            Best case: O(M)

        Space Complexity:
            Worst Case: O(M)
            Best case: O(M)
    """
    letters_in_alphabet = 26
    counter = [0]*letters_in_alphabet
    # Normal the ascii from 97 since at this number it is when "a" starts
    for i in range(len(word)):
        dec = char_to_dec(word[i])
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
    """
    Returns a list of words picked from wordlist that could be valid answers to a world question based on a given word and corresponding marker from the word

        Parameters:
            wordlist (list[str]): A list of possible choices of words for given wordle game
            word (str): A word that was previous inputted as a solution
            marker (list[int]): A list of integers of 1 or 0 where 1 means correct position and 0 means wrong position but exists inside the solution

        Returns:
            res (list[str]): a list of words picked from wordlist that could be valid answers to a world question based on a given word and corresponding marker from the word
    """
    letters_in_alphabet = 26 # There are currently 26 letters in the alphabet and goes from [a-z]
    counter_for_word = [0]*letters_in_alphabet # M auxiliary space complexity to store counter for word
    res = []

    # Counter for the letters in word
    for i in range(len(word)):
        dec = char_to_dec(word[i])
        counter_for_word[dec] += 1

    # Check for every word in wordlist and see if the arrays are equal M*N complexity
    for i in range(len(wordlist)): # N
        tmp_counter = count(wordlist[i])
        if tmp_counter == counter_for_word:
            same_positions = True
            for j in range(len(marker)): # m
                if marker[j] == 1 and word[j] != wordlist[i][j]:
                    same_positions = False
                    break
                elif marker[j] == 0 and word[j] == wordlist[i][j]:
                    same_positions = False
                    break

            if same_positions == True:
                res.append(wordlist[i])


    # Sort the answer into lexicographical order so O(M*N) worst case if all words in wordlist can be a solution
    for i in range(len(marker)):
        j = len(marker) - i - 1
        if marker[j] == 0:
            res = count_sort(res, j)

    print(res)
    return res


wordlist = ['costar', 'carets', 'recast', 'traces', 'reacts', 'caster', 'caters', 'crates', 'actors', 'castor']

word = 'catrse'
marker = [1,1,0,0,0,0]

print(trainer(wordlist, word, marker))

