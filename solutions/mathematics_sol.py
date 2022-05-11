import math


class MathematicsSolution:
    def fibonnaci(self, n):
        """
        Given an integer n, print the nth number in the
        fibonnaci sequence.
        """
        # if n happens to be 0 or 1, go back up recursive stack
        if n <= 1:
            return n
        
        return self.fibonnaci(n - 1) + self.fibonnaci(n - 2)

    
    def factorial(self, n):
        # if n happens to be 0 or 1, go back up recursive stack
        if n <= 1:
            return n

        return n * self.factorial(n - 1)

    
    def distance(self, x1, y1, x2, y2):
        """
        Calculate the euclidean distance between
        two points (x1, y1) and (x2, y2).
        """
        return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    

    def mean(self, numbers):
        """
        Given a set of numbers, calculate the arithmetic mean (average)
        of the numbers.
        """

        # sum object
        sum = 0

        # adds all numbers
        for number in numbers:
            sum += number
        
        # returns division of sum by number of numbers
        return sum / len(numbers)

    
    def max(self, numbers):
        """
        Given a set of numbers, return the maximum
        integer.
        """
        # maximum value is starting minimum
        max = -math.inf

        # if a number is lower than the curent
        # minimum, then that number becomes the
        # new minimum
        for number in numbers:
            if number > max:
                max = number
        
        return max
    

    def min(self, numbers):
        """
        Given a set of numbers, find the minimum
        integer.
        """

        # maximum value is starting minimum
        min = math.inf

        # if a number is lower than the curent
        # minimum, then that number becomes the
        # new minimum
        for number in numbers:
            if number < min:
                min = number
        
        return min

    
    def is_prime(self, num):
        """
        Given some number, check if the number is a
        prime number.
        """
        # if the number given is 0 or 1,
        # then it is not a prime number.
        if num <= 1:
            return False
        
        # if the number divides evenly
        # (no remainder) with a certain
        # factor, then it is by definition
        # composite (false)
        for i in range(2, num):
            if num % i == 0:
                return False

        return True
