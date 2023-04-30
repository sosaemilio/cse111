import csv
import json

import firebase_admin
from firebase_admin import credentials, db

# Sample Code Extracted from Firebase documentation
# Initiliaze Firebase using the private key
#
# Change the credentials and link below to test the script 
# the rest will work, don't forget to create a realtime database and set up a .indexOn rule to search queries.
# See more https://firebase.google.com/docs/database/security/indexing-data
cred = credentials.Certificate("API_KEY")
firebase_admin.initialize_app(cred, {'databaseURL': "https://example.com"})

def main():
    try:

        print("1. Import CSV ")
        print("2. Retrieve information ")
        option = int(input("Choose your option: "))

        if option == 1:
            # First option to import a CSV.
            filename = str(input("\nWhat is the filename(CSV) you want to import? "))
            json_file = convert_json(filename)
            import_data(json_file)
        elif option == 2:
            # Option #2 search sorting by name
            search_input = input("\nWhat name would you like to search? ")
            customer_information = retrieve_data(search_input)
            for key, value in customer_information.items():
                print(f"{key} : {value}")
    except FileNotFoundError as notFoundErr:
        print(notFoundErr)
    except ValueError as valError:
        print(valError)
    except IndexError as inError:
        print(f"{inError} - The name you wrote is too short or doesn't exist")
    


def convert_json(csv_name):
    """
    Function to convert a CSV file into a JSON file and string
    
    Arguments:
        csv_name = string with the CSV name and location.
    return
        json string
    """
    # Creates the dictionary
    json_list = []

    # Open CSV
    with open(csv_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            json_list.append(row)

    # Creates the .json filename
    json_filename = csv_name.rstrip(".csv")
    json_filename += ".json"

    with open(json_filename, "w+") as json_file:
        # Import the dictionary into the newly created JSON
        json.dump(json_list, json_file)

    # Pass the JSON file as a variable
    file_contents = json.load(open(json_filename, 'r'))

    return file_contents

def import_data(json_string):


    # Set the Firebase directory
    ref = db.reference("/customers")

    # Use the .set method to push the string json into Firebase
    ref.set(json_string)

    # Success message
    print(f"Sucesfully Imported the file.")


def retrieve_data(name):
    """
    Function to retrieve customer's information by the provided name.

    Arguments:
        Name: String with the name to search

    return:
        Dictionary with the customer information.
    """
    
    # Change the reference to the customer directory
    ref = db.reference("/customers")
    # Create a search query using the 'ContactName' as the key value or index,
    # this will start search from the name variable
    snapshot = ref.order_by_child("ContactName").start_at(name).get()

    firebase_id = list(snapshot.keys())[0]
    customer_information = snapshot[firebase_id]

    return customer_information
    
        

if __name__ == "__main__":
    main()