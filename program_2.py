# David Stalmakov, 10/30/2025
# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def main():
    try:
        count = int(input("How many random numbers do you want the file to hold (1-1000)?"))
        if count < 1 or count > 1000:
            print("Please enter a number between 1 and 1000")
            return
        with open("random_numbers.txt", "w") as file:
            for i in range(count):
                number = random.randint(1, 500)
                file.write(str(number) + "\n")

        print(f"{count} random numbers were added to 'random_numbers.txt'.")

    except ValueError:
        print("Please enter a valid integer.")
if __name__ == '__main__':
    main()