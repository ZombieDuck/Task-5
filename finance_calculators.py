# Task 5 - Capstone Project

# imports the math module to access mathematical functions
import math

# asks the user for an response based on the string
while True:
    answer = (input('''
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed:
      ''')).strip().lower() # Converts the input to lowercase and remove leading/trailing spaces

# if the user inputs 'investment' then ask the for responses to help calculate the total
    if answer == "investment":
        # using int before input on answers that require numbers to avoid trailing decimal numbers
        funds = int(input("How much are you depositing? "))
        interest_rate = float(input("What is the interest rate in %? (Enter only numbers) "))
        term = int(input("How many years do you plan to invest for? "))
        interest_type = (input("Would you like simple or compound interest applied? (Please enter 'simple' or 'compound') "))

        # nested if statement to calculate different responses depending on user input
        if interest_type == "simple":
            simple_total = int(funds * (1 + (interest_rate/100) *term))
            print(f"Your investment return will be £{simple_total}")
            break # stops the loop from running when completed formula
        elif interest_type == "compound":
            compound_total = int(funds * math.pow((1 + interest_rate/100), term))
            print(f"Your investment return will be £{compound_total}")
            break 
        else: 
            print("Invalid response") # if the user has not input the expected response, print error message

    elif answer == "bond":
        value = int(input("What is the present value of the house? "))
        b_interest_rate = int(input("What is the interest rate in %? (Enter only numbers) "))
        payback_length = int(input("How long would you like to pay back your loan? (in months) "))
        repayment = ((b_interest_rate/100)/12 * value)/(1 - (1 + (b_interest_rate/100)/12)**(-payback_length))
        print(f"You will have to pay back £{int(repayment)} per month.")
        break

    # if their answer is one of the options, break the loop. Otherwise, print error message.
    else: # answer not in ('investment', 'bond'):
        print("Invalid response, please enter either 'investment' or 'bond'.")
