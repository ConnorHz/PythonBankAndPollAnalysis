import os
import csv

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

totalVotes = 0
candidates = {}
winnerVotes = 0
winnerName = ''
candidateResults = ''

with open(os.path.join("PyPoll", "Resources", "election_data.csv")) as csvFile:

    csvreader = csv.reader(csvFile, delimiter=',')

    # Skip First Row
    next(csvreader)

    # Headers: Voter ID, County, Candidate
    for row in csvreader:
        totalVotes += 1

        if row[2] in candidates:
            candidates[row[2]]['Votes'] += 1
        else:
            candidates[row[2]] = {'Votes': 0, 'Percentage': 0}

# '%.3f'%

for candidate in candidates:
    # Calculate percentage of votes for each candidate
    candidates[candidate]['Percentage'] = (candidates[candidate]['Votes']/totalVotes)*100

    outPercentage = '{:.3f}'.format(round(candidates[candidate]['Percentage']))
    outVotes = candidates[candidate]['Votes']

    candidateResults = f'{candidateResults}{candidate}: {outPercentage}% ({outVotes})\n'

    # TODO Figure this out. Still unsure how to effectivly loop through a dictionary
    if candidates[candidate]['Votes'] > winnerVotes:
        winnerVotes = candidates[candidate]['Votes']
        winnerName = candidate

output = ("Election Results\n"
          "----------------------------\n"
         f"Total Votes: {totalVotes}\n"
         "----------------------------\n"
         f"{candidateResults}"
         "----------------------------\n"
         f"Winner: {winnerName}\n"
         "----------------------------"
        )

print(output)

f = open(r"PyPoll\analysis\ElectionResults.txt", "w")
f.write(output)
f.close()
        