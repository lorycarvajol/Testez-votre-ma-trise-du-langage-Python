def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The average of the numbers in the list.
    """
    if not numbers:
        return 0  # Return 0 if the list is empty to avoid division by zero

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
