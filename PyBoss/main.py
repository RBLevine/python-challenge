import os
import csv

# Create path for the file to be read
readPath=os.path.join('Resources', 'employee_data.csv')

# Create path for the file to be written to
writePath=os.path.join('Analysis','updated_employee_data.csv')

# Using dictionary from [Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5)
stateAbbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open the file using "write" mode. Specify the variable to hold the contents
with open(writePath, 'w', newline='') as writeFile:
    # Initialize csv.writer
    csvwriter = csv.writer(writeFile)
    with open(readPath) as readFile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(readFile, delimiter=',')

        # Read the header row first 
        csv_header = next(csvreader)

        # Write the first row (column headers)
        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name','DOB','SSN','State'])

        # Read each row of data after the header
        for row in csvreader:
            
            # Set empID to exactly what is is read file in column 0
            empID=row[0]

            # Take the name from read file and store as list, separating at the <space>
            name=row[1].split(" ")
            # Set firstName equal to the first item in the name list
            firstName=name[0]
            # Set lastName equal to the second itema in the name list
            lastName=name[1]

            # Take the dob from the read file and store as list, separating at the dash
            dob=row[2].split("-")
            # Reformat the dob to be in the appropriate format
            correctDOB=(f"{dob[1]}/{dob[2]}/{dob[0]}")

            # Take the ssn fromt he read file and store as list, separating at the dash
            ssn=row[3].split("-")
            # Reformat the ssn so that all but last 4 digits are displayed as *s
            correctSSN=(f"***-**-{ssn[2]}")

            # Store the state from the read file as the abbreviation accessed in the stateAbbrev dictionary
            state=stateAbbrev[row[4]]
            
            # Write into the file
            csvwriter.writerow([empID,firstName,lastName,correctDOB,correctSSN,state])







