import os
import csv

# Path for the budget data file
budgetData_csv = os.path.join( "Resources", "budget_data.csv")

# Initializing all variables used in code below
totalProLos=0
totalMonths=0
totalChange=0
lastProLos=0
recentChange=0
greatProfit=0
greatProfitMonth=""
greatLoss=0
greatLossMonth=""

# Open and read csv
with open(budgetData_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:

        # Track total number of months in dataset
        totalMonths+=1

        # Track net total amount of Profit/Losses
        totalProLos+=int(row[1])

        # Track average change in Profit/Losses
        # If we are on the first line, 
        if totalMonths==1:
            # Set the lastProLos variable to the Profit/Loss data in that row
            lastProLos=int(row[1])
        
        # If we are not on the first line, 
        else:
            # Calculate change between current line and previous line, 
            recentChange=int(row[1])-lastProLos
            # Add that to the running change total, 
            totalChange+=recentChange
            # Reset data for the lastProLos
            lastProLos=int(row[1])
       
        # Track greatest increase in profits (date and amount)
        # If recentChange is greater than currently stored greatProfit
        if recentChange>greatProfit:
            # Reset greatProfit to recentChange
            greatProfit=recentChange
            # Store the month associated with the greatProfit/recentChange
            greatProfitMonth=str(row[0])     
                  
        # Track greatest decrease in losses (date and amount)
        # If recent change is less than currently stored greatLoss
        elif recentChange<greatLoss:
            # Reset greatLoss to recentChange
            greatLoss=recentChange
            # Store the month associated with the greatLoss/recentChange
            greatLossMonth=str(row[0]) 

#calculate average change
averageChange="%.2f" % (totalChange/(totalMonths-1))

# Specify the file to write to
output_path = os.path.join("Analysis", "PyBankResults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    print("Financial Analysis", file=txtfile) 
    print("Financial Analysis") 
    print("-------------------------", file=txtfile)
    print("-------------------------")
    print(f"Total Months: {totalMonths}", file=txtfile)
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalProLos}", file=txtfile)
    print(f"Total: ${totalProLos}")
    print(f"Average Change: ${averageChange}", file=txtfile)
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits: {greatProfitMonth} (${greatProfit})", file=txtfile)
    print(f"Greatest Increase in Profits: {greatProfitMonth} (${greatProfit})")
    print(f"Greatest Decrease in Profits: {greatLossMonth} (${greatLoss})", file=txtfile)
    print(f"Greatest Decrease in Profits: {greatLossMonth} (${greatLoss})")