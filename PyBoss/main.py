import os
import csv

us_state_abbrev = {
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

with open(os.path.join("PyBoss", "Resources", "employee_data.csv")) as csvFile:
    
    csvreader = csv.reader(csvFile, delimiter=',')

    next(csvreader)

    with open(os.path.join("PyBoss", "output", "formatted_employee_data.csv"), 'w') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',')

        csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

        for row in csvreader:
            firstName = row[1].split(' ')[0]
            lastName = row[1].split(' ')[1]
            dateOfBirth = f"{row[2].split('-')[1]}/{row[2].split('-')[2]}/{row[2].split('-')[0]}"
            ssn = f"***-**-{row[3].split('-')[2]}"
            state = us_state_abbrev[row[4]]

            csvwriter.writerow([row[0], firstName, lastName, dateOfBirth, ssn, state])