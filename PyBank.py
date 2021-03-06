import csv 
import os 

# Uploading File
filepath = os.path.join("budget_data.csv")


# Read the csv and convert it into a list of dictionaries
with open(filepath) as budget_data:
    reader = csv.reader(budget_data)

    # use of next to skip first title row in csv file
    next(reader) 
    revenue = []
    date = []
    change = []
    change_date = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:

        revenue.append(float(row[1]))
        date.append(row[0])
    
    print("-----------------------------------")
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Month:", len(date))
    print("Total $", round(sum(revenue)))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])   
        change_date.append(date[i])

        avgchange = sum(change)/len(change)
        maxchange = max(change)

        minchange = min(change)
        maxchange_date = change_date[change.index(max(change))]
        minchange_date = change_date[change.index(min(change))]
      


    print("Avereage Change: $", round(avgchange,2))
    print("Greatest Increase in Profits:", maxchange_date,"($",round( maxchange),")")
    print("Greatest Decrease in Profits:", minchange_date,"($",round( minchange),")")
    print("-----------------------------------")

