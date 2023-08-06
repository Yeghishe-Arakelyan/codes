def palindrome():
    """
    Checks if the entered word is a palindrome.

    The function takes user input for a word, converts it to lowercase,
    and checks if it is the same forwards and backwards (a palindrome).

    Example:
        Input: "level"
        Output: True
    """
    word = input('Enter word: ')
    word = word.lower()
    return print(word == word[::-1])
        
palindrome()