import os
import csv

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

totalVotes = 0
candidates = {}
winner = { 'Name': {'Votes': 0}}

with open(os.path.join("PyPoll", "Resources", "election_data.csv")) as csvFile:

    csvreader = csv.reader(csvFile, delimiter=',')

    # Skip First Row
    next(csvreader)

    #Headers: Voter ID, County, Candidate

    for row in csvreader:
        totalVotes += 1

        if row[2] in candidates:
            candidates[row[2]]['Votes'] += 1
        else:
            candidates[row[2]] = {'Votes': 0, 'Percentage': 0}

for candidate in candidates:
    # TODO Figure this out. Still unsure how to effectivly loop through a dictionary
    candidates[candidate]['Percentage'] = (candidates[candidate]['Votes']/totalVotes)*100
    if candidates[candidate]['Votes'] > winner[0]['Votes']:
        winner[0] = { 'Name': candidate {'Votes': candidates[candidate]['Votes']}}

print(winner)
print(candidates)
        