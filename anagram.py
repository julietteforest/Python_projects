
"""
finding anagramm
10/2019
Author:
        Juliette Forest
"""

from itertools import permutations
def anagram(word): #enter your word inside "word"
    propositions = list(permutations(word)) #permutating the letters
    for anagram in propositions:
        print(' '.join(anagram)) #printin the list of annagrams

"""

anagramm("hot")
    h o t
    h t o
    o h t
    o t h
    t h o
    t o h

"""
