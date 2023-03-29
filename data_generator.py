import random

class DataGenerator:
    def __init__(self, count):
        self.count = count

    def generate_random_numbers(self):
        """
        This method generates a list of random numbers between 1 and 100.
        """
        random_numbers = [random.randint(1, 100) for _ in range(self.count)]
        return random_numbers

    def generate_normal_distribution(self, mean, std):
        """
        This method generates a list of numbers from a normal distribution with a given mean and standard deviation.
        """
        normal_numbers = np.random.normal(loc=mean, scale=std, size=self.count)
        return normal_numbers

    def generate_exponential_distribution(self, rate):
        """
        This method generates a list of numbers from an exponential distribution with a given rate.
        """
        exponential_numbers = np.random.exponential(scale=1/rate, size=self.count)
        return exponential_numbers

    def generate_poisson_distribution(self, rate):
        """
        This method generates a list of numbers from a Poisson distribution with a given rate.
        """
        poisson_numbers = np.random.poisson(lam=rate, size=self.count)
        return poisson_numbers
