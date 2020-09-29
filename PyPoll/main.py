import os
import csv

electData_csv = os.path.join("Resources", "election_data.csv")
totalVotes=0
# Key is 
electDict={}
highVote=0
highVoteName=""

# Open and read csv
with open(electData_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        # Track total number of votes cast
        totalVotes+=1
        # List of candidates with votes
        # Total number of votes each candidate won
        if row[2] in electDict:
            electDict[row[2]]+=1
        else:
            electDict[row[2]]=1
        

# Print report
# Specify the file to write to
output_path = os.path.join("Analysis", "PyPollResults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    print("Election Results", file=txtfile)
    print("Election Results")
    print("----------------------", file=txtfile)
    print("----------------------")
    print(f"Total Votes: {totalVotes}", file=txtfile)
    print(f"Total Votes: {totalVotes}")
    print("----------------------", file=txtfile)
    print("----------------------")
    for key in electDict:
        percent="{:.3%}".format(electDict[key]/totalVotes)
        # Percentage of votes each candidate won
        # Winner of election based on popular vote
        print(f"{key}: {percent} ({electDict[key]})", file=txtfile)
        print(f"{key}: {percent} ({electDict[key]})")
        # Find the winner
        if electDict[key]>highVote:
            highVote=electDict[key]
            highVoteName=key
    print("----------------------", file=txtfile)
    print("----------------------")
    print(f"Winner: {highVoteName}", file=txtfile)
    print(f"Winner: {highVoteName}")
    print("----------------------", file=txtfile)
    print("----------------------")
