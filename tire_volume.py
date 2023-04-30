"""
Emilio Sosa - W02 Prove Assigment 
Programming with Functions CS111 - Section 14

"""

# Import neccesary libraries one for the math calculations (PI) and one for the current date
from datetime import datetime
import math

# Last Week Assigment
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_radio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = round((math.pi * (width ** 2)  * aspect_radio * (width * aspect_radio + 2540 * diameter)) / (10000000000), 2)

print(f"The approximate volume is {volume} liters")


## Exceeding the Requirements
purchase = str(input("\nWould you like to buy a tire using the provided dimension? "))
if purchase.lower() == "yes":
    phone_number = str(input("What is your phone number? "))

# W02 - Assigment
current_day = datetime.now(tz=None)

# Open or Creates the file using append mode and stored it in a value
with open("volumes.txt", "at") as volume_file:

    # Depending if she provided or not her phone number one of the followed condition will be executed.
    if purchase.lower() == "yes":
        print(f"{current_day:%Y-%m-%d}, {width}, {aspect_radio}, {diameter}, {volume}, {phone_number}", file=volume_file)
    else:
        print(f"{current_day:%Y-%m-%d}, {width}, {aspect_radio}, {diameter}, {volume}", file=volume_file)
