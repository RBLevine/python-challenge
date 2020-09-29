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
        
#file=open("Analysis","PyPollResults.txt","w")
# Print report
#file.write("Election Results")
print("Election Results")
#file.write("----------------------")
print("----------------------")
#file.write(f"Total Votes: {totalVotes}")
print(f"Total Votes: {totalVotes}")
#file.write("----------------------")
print("----------------------")
for key in electDict:
    percent="{:.3%}".format(electDict[key]/totalVotes)
     # Percentage of votes each candidate won
    # Winner of election based on popular vote
 #   file.write(f"{key}: {percent} ({electDict[key]})")
    print(f"{key}: {percent} ({electDict[key]})")
    # Find the winner
    if electDict[key]>highVote:
        highVote=electDict[key]
        highVoteName=key
#file.write("----------------------")
print("----------------------")
#file.write(f"Winner: {highVoteName}")
print(f"Winner: {highVoteName}")
#file.write("----------------------")
print("----------------------")
#file.close()
