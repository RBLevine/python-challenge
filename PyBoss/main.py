import os
import csv

readPath=os.path.join('Resources', 'employee_data.csv')
writePath=os.path.join('Analysis','updated_employee_data.csv')
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

        # Read the header row first (skip this step if there is now header)
        csv_header = next(csvreader)
        # Write the first row (column headers)
        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name','DOB','SSN','State'])

        # Read each row of data after the header
        for row in csvreader:
            empID=row[0]
            name=row[1].split(" ")
            firstName=name[0]
            lastName=name[1]
            dob=row[2].split("-")
            correctDOB=(f"{dob[1]}/{dob[2]}/{dob[0]}")
            ssn=row[3].split("-")
            correctSSN=(f"***-**-{ssn[2]}")
            state=stateAbbrev[row[4]]
            
            # Write into the file
            csvwriter.writerow([empID,firstName,lastName,correctDOB,correctSSN,state])







