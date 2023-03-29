import random

def generate_random_numbers(n):
    """
    This function generates n random numbers between 1 and 100 and returns them in a list.
    """
    random_numbers = []
    for i in range(n):
        random_numbers.append(random.randint(1, 100))
    return random_numbers

def calculate_mean(numbers):
    """
    This function calculates the mean of a list of numbers.
    """
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

def calculate_median(numbers):
    """
    This function calculates the median of a list of numbers.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2] + sorted_numbers[n//2-1]) / 2
    else:
        median = sorted_numbers[n//2]
    return median

def calculate_mode(numbers):
    """
    This function calculates the mode of a list of numbers.
    """
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    max_count = max(count_dict.values())
    mode = [number for number, count in count_dict.items() if count == max_count]
    return mode[0]

if __name__ == "__main__":
    # Generate a list of 10 random numbers
    random_numbers = generate_random_numbers(10)

    # Calculate the mean, median, and mode of the list
    mean = calculate_mean(random_numbers)
    median = calculate_median(random_numbers)
    mode = calculate_mode(random_numbers)

    # Print the results
    print("Random numbers:", random_numbers)
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
