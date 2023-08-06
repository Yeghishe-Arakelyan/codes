def create_acronym():
    """
    Generates an acronym from the given input string.

    The function takes a user input string, splits it into words, and creates
    an acronym by taking the first letter of each word and converting it to uppercase.

    Example:
        Input: "International Business Machines"
        Output: "IBM"
    """
    string = input('Enter your string: ')
    words = string.split()
    acronym = ''.join(word[0].upper() for word in words)
    print(acronym)

create_acronym()
