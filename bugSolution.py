def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")  # Raise exception for clarity
    return sum(numbers) / len(numbers)

try:
    my_list = []
    average = calculate_average(my_list)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")  # Handle the exception