from statistics import DataAnalyticsTool
from data_generator import DataGenerator

def main():
    # Generate a list of 10 random numbers
    data_generator = DataGenerator
    random_numbers = data_generator.generate_random_numbers()

    # Create a DataAnalyticsTool instance using the random numbers
    data_tool = DataAnalyticsTool(random_numbers)

    # Calculate the mean, median, mode, standard deviation, variance, skewness, kurtosis, range, interquartile range, and z-scores
    mean = data_tool.calculate_mean()
    median = data_tool.calculate_median()
    mode = data_tool.calculate_mode()
    std = data_tool.calculate_standard_deviation()
    var = data_tool.calculate_variance()
    skew = data_tool.calculate_skewness()
    kurtosis = data_tool.calculate_kurtosis()
    data_range = data_tool.calculate_range()
    iqr = data_tool.calculate_interquartile_range()
    z_scores = data_tool.calculate_z_scores()

    # Print the results
    print("Random numbers:", random_numbers)
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Standard deviation:", std)
    print("Variance:", var)
    print("Skewness:", skew)
    print("Kurtosis:", kurtosis)
    print("Range:", data_range)
    print("Interquartile range:", iqr)
    print("Z-scores:", z_scores)

if __name__ == "__main__":
    main()
