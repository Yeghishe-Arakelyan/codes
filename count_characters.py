def count_characters():
    """
    Counts the occurrences of each character in the given word or string.

    The function takes a user input word or string and creates a dictionary
    that maps each character to its respective count.

    Example:
        Input: "hello"
        Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    string = input('Enter word: ')
    count_dict = {}

    for i in string:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    print(count_dict)

count_characters()