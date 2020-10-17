import csv
import os

# Uploading File
filepath = os.path.join("election_data.csv")

total_votes = 0

# Candidates
candidate_options =[]
candidate_votes = {}

winning_candidate =""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(filepath) as election_data:
    reader = csv.reader(election_data)

    # use of next to skip first title row in csv file
    header =  next(reader)
    
    for row  in reader:
        total_votes += 1
        candidate_name = row[2]

        # If candidate name not in the list create his name and add a vote to his count
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] += 1

 # Printing Total number of Votes

print("-----------------------------------")
print("Election Results")
print("-----------------------------------")
print("Total Votes:"+str(total_votes))
print("-----------------------------------")

# printing stats for all the candidate on the candidate name and rounding it the closest percentage with total number of votes each candidate recieved.
for candidate in candidate_votes:

    votes = candidate_votes.get(candidate)
    vote_percentage = round(float(votes) / float(total_votes) * 100)
    if (votes > winning_count):
        winning_count = votes
        winning_candidate = candidate

    output = f"{candidate}: {vote_percentage: .2f}% ({votes})\n"
    print(output)
   
print("-----------------------------------")
print("Winner:", winning_candidate)
print("-----------------------------------")
