def anagram_or_not():
    """
    Checks if two input words are anagrams of each other.

    The function takes user input for two words, converts them to lowercase,
    and checks if they are anagrams by comparing their sorted forms.

    Example:
        Input: First word = "listen", Second word = "silent"
        Output: True
    """
    w1 = input('Enter first word: ')
    w2 = input('Enter second word: ')
    w1 = w1.lower()
    w2 = w2.lower()

    return print(sorted(w1) == sorted(w2))

anagram_or_not()