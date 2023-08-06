def zodiac_name():
    """
    Determines the zodiac sign based on the input birth month and day.

    The function takes user input for the birth month and day and then
    prints the corresponding zodiac sign.

    Example:
        Input: Birth month = 7, Birth day = 23
        Output: Leo
    """
    month = int(input('Enter your birth month (1-12): '))
    day = int(input('Enter your day of birth (1-31): '))
    zodiac_signs = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21))
    ]
    for x, (start_month, start_day), (end_month, end_day) in zodiac_signs:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            print(x)

zodiac_name()

