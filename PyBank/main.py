import os
import csv

budgetData_csv = os.path.join("..", "Resources", "budget_data.csv")
totalProLos=0
totalMonths=0
totalChange=0
lastProLos=0

# Open and read csv
with open(budgetData_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

        # Track total number of months in dataset
        totalMonths+=1
        # Track net total amount of Profit/Losses
        totalProLos+=rows[1]
        # Track average change in Profit/Losses

        # Track greatest increase in profits (date and amount)

        # Track greatest decrease in losses (date and amount)

    
    # Print out results to Terminal
