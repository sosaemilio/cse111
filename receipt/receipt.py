import csv
from datetime import datetime

KEY = 0

def main():
    try:
        products_dic = read_dict("products.csv", KEY)
        print("Inkom Emporium")

        print(f"\nRequested Items ")
        
        current_date_and_time = datetime.now()

        with open("request.csv") as file:
            requests = csv.reader(file)
            next(requests)
            
            ordered_items = 0
            subtotal = 0
            for request in requests:
                PRODUCT_KEY = request[0]
                quantity = int(request[1])

                product_data = products_dic[PRODUCT_KEY]

                product_name = product_data[1]
                product_price = float(product_data[2])

                print(f"{product_name}: {quantity} @ {product_price}")
                ordered_items += quantity
                subtotal += quantity * product_price

            print(f"\nNumber of Items: {ordered_items}")
            
            # Get the current day of the week using the objet weekday and return a integer
            day_week = current_date_and_time.weekday()

            # If the weekday is Tuesday or Wedneday it will give a 10% of discount
            if day_week == 1 or day_week == 2:
                day_week = current_date_and_time.weekday()
                discount = ((subtotal * 10) / 100)
                subtotal = discount - subtotal

                print(f"Today is {day_week}, you get a 10% of discount today")
                print(f"Discount: {round(discount, 2)}")

                print(f"\nSubtotal: {round(subtotal, 2)}")
            else:
                print(f"Subtotal: {round(subtotal, 2)}")

            sales_taxes = (subtotal * 6) / 100
            total = subtotal + sales_taxes

            print(f"Sales Tax (6%): {round(sales_taxes, 2)}")
            print(f"Total: {round(total, 2)}")

            print(f"\nThank you for shopping at the Inkom Emporium. ")
            print(f"{current_date_and_time:%c}")
    
    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except PermissionError as permision_denied:
        print(permision_denied)
    except KeyError as error:
        print(f"Error: unknown product ID in the request.csv file {error}")




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

    dictonary = {}

    with open(filename) as file:
        # Create a open with the ability to read the file
        reader = csv.reader(file)

        # Jump the first row
        next(reader)

        for row in reader:
            if row != 0:
                key = row[key_column_index]
                dictonary[key] = row

    return dictonary

if __name__ == "__main__":
    main()