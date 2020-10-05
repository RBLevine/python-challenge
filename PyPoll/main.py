import os
import csv

# Create read file path
electData_csv = os.path.join("Resources", "election_data.csv")

# Initialize variables
totalVotes=0
electDict={}
highVote=0
highVoteName=""

# Open and read csv
with open(electData_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        # Track total number of votes cast
        totalVotes+=1

        # Check if the Candidate's name is in the dictionary
        if row[2] in electDict:
            # If it is, add one to the votes associated with that candidate
            electDict[row[2]]+=1
        else:
            # If they are not, add them and set their votes equal to 1
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

    # Run through all candidates in the dictionary
    for key in electDict:
        # Calculate the percent of votes they got
        percent="{:.3%}".format(electDict[key]/totalVotes)

        print(f"{key}: {percent} ({electDict[key]})", file=txtfile)
        print(f"{key}: {percent} ({electDict[key]})")
        # Find the winner
        # If the number of votes for the current Candidate is greater than the stored highVote
        if electDict[key]>highVote:
            # Set the highVote equal to the number of votes the current Candidate has
            highVote=electDict[key]
            # Store the name of the current Candidate
            highVoteName=key
            
    print("----------------------", file=txtfile)
    print("----------------------")

    print(f"Winner: {highVoteName}", file=txtfile)
    print(f"Winner: {highVoteName}")

    print("----------------------", file=txtfile)
    print("----------------------")
