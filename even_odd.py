def even_odd():
    """
    Checks if the entered number is even or odd.

    The function takes user input for a number and prints whether it is an
    even or odd number.

    Example:
        Input: 7
        Output: Odd number!
    """
    number = int(input('Enter number: '))
    if number % 2 == 0:
        print('Even number!')
    else:
        print('Odd number!')

even_odd()