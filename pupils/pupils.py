import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
    students_list = read_compound_list("pupils.csv")

    student_birthday = lambda student_information: student_information[BIRTHDATE_INDEX]
    students_list = sorted(students_list, key=student_birthday)

    # print_list(students_list)

    student_given_name = lambda student_information: student_information[GIVEN_NAME_INDEX]
    students_list = sorted(students_list, key =  student_given_name)

    # print_list(students_list)

    sorted_list_3 = month_day(students_list)

    # students_list = sorted(students_list, key = month_day)
    
    print_list(sorted_list_3)



def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(list_file):
    """
    Functions that reads a CSV and print the rows one by one
    
    Parameter
        List_file: is a csv file

    return: nothing
    """

    for line in list_file:
        print(line)


def month_day(students):

    birthday = students[BIRTHDATE_INDEX]
    month_day = birthday[5:]

    sorted(students, key = month_day)
    return month_day

if __name__ == "__main__":
    main()