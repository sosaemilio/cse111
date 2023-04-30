"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.
"""
import datetime

subtotal = 0

i = 1
while i >= 1:
    price =  float(input("What is the price: "))
    qty = int(input("What is the quantity: "))
    if qty == 0:
        i = 0

    subtotal = (price * qty) + subtotal

    # subtotal = float(input("What is the subtotal: "))

    today = datetime.datetime.now(tz=None)
    day = datetime.datetime.weekday(today)

    if day == 1 and subtotal >= 50:
        subtotal = subtotal - ((subtotal * 10) / 100)   
    elif day == 2 and subtotal >= 50:
        subtotal = subtotal - ((subtotal * 10) / 100)
    elif day == 1 and subtotal < 50:
        amount = 50 - subtotal
        print(f"To get a discount you need to spend {amount}")
    elif day == 2 and subtotal < 50:
        amount =  50 - subtotal
        print(f"To get a discount you need to spend {amount}")


    tax = (subtotal * 6) / 100

    total = tax + subtotal



    print(f"Please enter the subtotal: {round(subtotal, 3)} ")
    print(f"Sales tax amount: {round(tax, 3)}")
    print(f"Total: {round(total, 3)}")