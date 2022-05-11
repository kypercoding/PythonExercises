import random


from exercises.mathematics_student import MathematicsStudent
from solutions.mathematics_sol import MathematicsSolution


class ValidateMathematics:
    def validate_implementation(self, m):
        """
        Perform preliminary checks on the mathematics
        implementations.
        """
        assert(m is not None)
    

    def test_mathematics(self):
        student = MathematicsStudent()
        solution = MathematicsSolution()

        self.validate_implementation(student)
        self.validate_implementation(solution)

        # generates random number for fibonnaci sequence
        # between 1-50
        n = random.randint(0, 50)

        # ensures fibonnaci is same between solution
        # and student
        f1 = student.fibonnaci(n)
        f2 = solution.fibonnaci(n)

        assert(f1 == f2)

        # generates random number for factorial between
        # 1-10
        n = random.randint(0, 10)

        # ensures factorial is same between solution
        # and student
        f1 = student.factorial(n)
        f2 = solution.factorial(n)

        assert(f1 == f2)

        # generates random x1, x2, y1, y2
        x1 = random.randint(0, 100)
        x2 = random.randint(0, 100)
        y1 = random.randint(0, 100)
        y2 =random.randint(0, 100)

        # ensures euclidean distance is same between
        # solution and student
        e1 = student.distance(x1, y1, x2, y2)
        e2 = solution.distance(x1, y1, x2, y2)

        assert(e1 == e2)

        # generates random list of numbers
        size = random.randint(0, 50)
        nums = []

        for _ in range(0, size):
            nums.append(random.randint(0, 1000))


        # ensures mean, minimum, and maximum return
        # same values
        assert(student.mean(nums) == solution.mean(nums))
        assert(student.min(nums) == solution.min(nums))
        assert(student.max(nums) == solution.max(nums))

        # generates ranodm number
        n = random.randint(0, 100)

        # ensures isPrime() returns the same for both
        # implementations
        assert(student.is_prime(n) == solution.is_prime(n))
