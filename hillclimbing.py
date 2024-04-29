# Hill climbing 

def simple_hill_climbing(numbers):
    current_index = 0
    while True:
        # Check if next index is within the list range
        if current_index + 1 < len(numbers):
            # Compare with the next number
            if numbers[current_index] < numbers[current_index + 1]:
                current_index += 1
            else:
                # Current number is greater than the next
                return numbers[current_index]
        else:
            # End of the list
            return numbers[current_index]
# Example list of numbers
numbers = [1, 3, 7, 12, 9, 5]
max_number = simple_hill_climbing(numbers)
print(f"The maximum number in the list is: {max_number}")
