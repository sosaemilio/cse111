import csv


NAME_INDEX = 0

def main():
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")

    i_number = i_number.replace("-", "")

    if not i_number.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(i_number) < 9:
            print("Invalid I-Number: too few digits ")
        elif len(i_number) > 9:
            print("Invalid I-Number: too many digits")
        else:
            students_dic = read_dict("students.csv", NAME_INDEX)
            
            if i_number in students_dic:
                students = students_dic[i_number]
                print(students[1])
            else: 
                print("No such student")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open(filename, "rt") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader: 
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row
    return dictionary

if __name__ == "__main__":
    main()