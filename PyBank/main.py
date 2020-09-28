import os
import csv

budgetData_csv = os.path.join( "Resources", "budget_data.csv")
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
        if totalMonths==1:
            lastProLos=int(row[1])
        else:
            recentChange=int(row[1])-lastProLos
            totalChange+=recentChange
            lastProLos=int(row[1])
        # Track greatest increase in profits (date and amount)
        if recentChange>greatProfit:
            greatProfit=recentChange
            greatProfitMonth=str(row[0])           
        # Track greatest decrease in losses (date and amount)
        elif recentChange<greatLoss:
            greatLoss=recentChange
            greatLossMonth=str(row[0]) 
#calculate average change
averageChange="%.2f" % (totalChange/(totalMonths-1))
# Print out results to Terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Month:{totalMonths}")
print(f"Total: ${totalProLos}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {greatProfitMonth} (${greatProfit})")
print(f"Greatest Decrease in Profits: {greatLossMonth} (${greatLoss})")