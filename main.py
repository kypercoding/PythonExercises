from validation.validate_ball_sort import ValidateBallSorter
from validation.validate_math import ValidateMathematics


def main():
    b = False

    while not b:
        prompt = input("Please enter test you wish to do: ")

        print("Loading...")

        if prompt == "BallSorter":
            v = ValidateBallSorter()
            v.test_ball_sorter()
        elif prompt == "Mathematics":
            m = ValidateMathematics()
            m.test_mathematics()
        elif prompt == "":
            b = True
        else:
            continue
            
        print("Done!")


if __name__ == "__main__":
    main()
