def calculate_percentage():
    """
    Calculates the percentage of a part in relation to the total.

    The function prompts the user to input the total value and the part value,
    then calculates the percentage as (part_value / total_value) * 100, and
    prints the result with two decimal places.

    Example:
        Input: Total value = 150, Part value = 30
        Output: The percentage is: 20.00%
    """
    total_value = float(input('Enter total value: '))
    part_value = float(input('Enter part value: '))

    percentage = (part_value/total_value)*100

    return print(f"The percentage is: {percentage:.2f}%")


def calculate_value_percentage():
    """
    Calculates the value of a percentage in relation to the total.

    The function prompts the user to input the total value and the percentage value,
    then calculates the value as (percentage_value / 100) * total_value, and
    prints the result.

    Example:
        Input: Total value = 1000, Percentage value = 10
        Output: 10% of 1000 is: 100.0
    """
    total_value = float(input('Enter total value: '))
    percentage_value = float(input('Enter percentage value: '))

    result = (percentage_value/100) * total_value
    return print(f"{percentage_value}% of {total_value} is: {result:.2f}")

calculate_percentage()
calculate_value_percentage()