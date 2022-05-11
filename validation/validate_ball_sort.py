import random


from solutions.ball_sorter_sol import BallSorterSolution
from exercises.ball_sorter_student import BallSorterStudent


class ValidateBallSorter:
    def validate_implementation(self, b):
        """
        Run preliminary tests on implementations of
        BallSorter.
        """
        assert(b is not None)

        assert(b.get_red_balls() is not None)
        assert(b.get_blue_balls() is not None)
        assert(b.get_green_balls() is not None)
    

    def test_ball_sorter(self):
        # student implementation
        student = BallSorterStudent()
        # solution implementation
        solution = BallSorterSolution()

        self.validate_implementation(student)
        self.validate_implementation(solution)

        # creates random choices for balls
        colors = ['R', 'G', 'B']

        # generates random array of balls
        balls = []

        size = random.randint(0, 1000)

        for _ in range(0, size):
            balls.append(random.choice(colors))

        # calls sorting implementations of student
        # and solution
        student.sort(balls)
        solution.sort(balls)

        assert(student.get_blue_balls() == solution.get_blue_balls())
        assert(student.get_green_balls() == solution.get_green_balls())
        assert(student.get_red_balls() == solution.get_red_balls())
