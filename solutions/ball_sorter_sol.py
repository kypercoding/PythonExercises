class BallSorterSolution:
    def __init__(self):
        """
        Initializes BallSorterSolution class
        with bins of red, green, and blue balls.
        """
        self.red = []
        self.green = []
        self.blue = []
    

    def sort(self, balls):
        """
        Given a set of R,G,B balls, the BallSorter
        sorts the balls into three different bins.
        """

        # for every ball in the original set, it is
        # placed in separate lists based on color
        for ball in balls:
            if ball == "R":
                self.red.append(ball)
            elif ball == "G":
                self.green.append(ball)
            else:
                self.blue.append(ball)
    

    def get_red_balls(self):
        """
        Returns set of red balls.
        """
        return self.red


    def get_blue_balls(self):
        """
        Returns set of blue balls.
        """
        return self.blue
    

    def get_green_balls(self):
        """
        Returns set of green balls.
        """
        return self.green
