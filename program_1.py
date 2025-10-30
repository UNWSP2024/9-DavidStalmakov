# David Stalmakov, 10/29/2025
# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    with open('names.txt', 'r') as file:
        lines = file.readlines()
        count = len(lines)
        print(f"There are {count} names in the file.")
            ######################
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()