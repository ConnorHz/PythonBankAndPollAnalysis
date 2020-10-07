# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
import os
import csv

totalMonths = 0
netTotalAmount = 0
profitLossChanges = []
lastRow = []
totalChanges = 0
greatestProfit = 0
greatestLoss = 0

strGreatestProfit = ""
strGreatestLoss = ""

with open(os.path.join("PyBank", "Resources", "budget_data.csv")) as csvFile:

    csvreader = csv.reader(csvFile, delimiter=',')

    # Skip First Row
    next(csvreader)

    for row in csvreader:
        totalMonths += 1
        netTotalAmount += int(row[1])

        if len(lastRow) != 0:
            profitLossChanges.append({'Month': row[0], 'Change': int(row[1]) - int(lastRow[1])})

        lastRow = row

for i in range(len(profitLossChanges)):

    totalChanges += profitLossChanges[i]["Change"]

    if profitLossChanges[i]["Change"] > greatestProfit:
        greatestProfit = profitLossChanges[i]["Change"]
        strGreatestProfit = "Greatest Increase in Profits: " + profitLossChanges[i]["Month"] + " ($" + str(profitLossChanges[i]["Change"]) + ")"

    if profitLossChanges[i]["Change"] < greatestLoss:
        greatestLoss = profitLossChanges[i]["Change"]
        strGreatestLoss = "Greatest Decrease in Profits: " + profitLossChanges[i]["Month"] + " ($" + str(profitLossChanges[i]["Change"]) + ")"

output = ("Financial Analysis\n"
          "----------------------------\n"
         f"Total Months: {totalMonths}\n"
         f"Total: ${netTotalAmount}\n"
         f"Average Change: ${round(totalChanges/len(profitLossChanges), 2)}\n"
         f"{strGreatestProfit} \n"
         f"{strGreatestLoss} \n"
        )

print(output)

f = open(r"PyBank\analysis\FinancialAnalysis.txt", "w")
f.write(output)
f.close()


     
