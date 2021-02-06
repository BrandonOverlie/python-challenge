import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

# lists to store data
candidate_vote = []
Khan_votes = []
Correy_votes = []
Li_votes = []
OTooley_votes = []

with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # get rid of header in csv
    csv_header = next(csv_file)

    # read through each row in csv
    for row in csv_reader:
        
        # create list for all votes cast for any candidate
        candidate_vote.append(row[2])

        # create lists for each candidate to store their votes
        if row[2] == 'Khan':
            Khan_votes.append(row[2])
        
        elif row[2] == 'Correy':
            Correy_votes.append(row[2])

        elif row[2] == 'Li':
            Li_votes.append(row[2])

        elif row[2] == "O'Tooley":
            OTooley_votes.append(row[2])

# use the length function to determine how many votes for each candidate using their individual lists created above
total_votes = len(candidate_vote)
total_Khan_votes = len(Khan_votes)
total_Correy_votes = len(Correy_votes)
total_Li_votes = len(Li_votes)
total_OTooley_votes = len(OTooley_votes)

#verified all votes accounted for by adding candidate votes together to see if it = total_votes (it does)
#print(total_Li_votes + total_Khan_votes + total_Correy_votes + total_OTooley_votes)

# % of votes cast for each candidate
Khan_vote_percent = total_Khan_votes / total_votes
Correy_vote_percent = total_Correy_votes / total_votes
Li_vote_percent = total_Li_votes / total_votes
OTooley_vote_percent = total_OTooley_votes / total_votes

# list of number of votes per candidate
candidate_votes_list = [['Khan', total_Khan_votes], ['Correy', total_Correy_votes], ['Li', total_Li_votes], ["O'Tooley", total_OTooley_votes]]
votes_list = [total_Khan_votes, total_Correy_votes, total_Li_votes, total_OTooley_votes]

# grab the winning vote count
for votes in votes_list:
    winner = max(votes_list)

#grab the candidate with the winning vote count
for candidate in candidate_votes_list:
    if candidate[1] == winner:
        Winning_Candidate = candidate[0]

# reformat variables
total_votes = '{:,}'.format(total_votes)
total_Khan_votes = '{:,}'.format(total_Khan_votes)
total_Correy_votes = '{:,}'.format(total_Correy_votes)
total_Li_votes = '{:,}'.format(total_Li_votes)
total_OTooley_votes = '{:,}'.format(total_OTooley_votes)
Khan_vote_percent = '{:.1%}'.format(Khan_vote_percent)
Correy_vote_percent = '{:.1%}'.format(Correy_vote_percent)
Li_vote_percent = '{:.1%}'.format(Li_vote_percent)
OTooley_vote_percent = '{:.1%}'.format(OTooley_vote_percent)

print (f'''
Election Results
------------------------------------------------
Total Votes Cast: {total_votes}
------------------------------------------------
                % of total votes  (total votes)
Khan Votes:         {Khan_vote_percent}          ({total_Khan_votes})
Correy Votes:       {Correy_vote_percent}          ({total_Correy_votes})
Li Votes:           {Li_vote_percent}          ({total_Li_votes})
O'Tooley Votes:     {OTooley_vote_percent}           ({total_OTooley_votes})
------------------------------------------------
Winning Candidate:  {Winning_Candidate}
------------------------------------------------
''')    

with open("election_results_report.txt", 'w') as txt_file:
    txt_file.write(f'''
    \n Election Results
    \n ------------------------------------------------
    \n Total Votes Cast: {total_votes}
    \n ------------------------------------------------
    \n                 % of total votes  (total votes)
    \n Khan Votes:         {Khan_vote_percent}          ({total_Khan_votes})
    \n Correy Votes:       {Correy_vote_percent}          ({total_Correy_votes})
    \n Li Votes:           {Li_vote_percent}          ({total_Li_votes})
    \n O'Tooley Votes:     {OTooley_vote_percent}           ({total_OTooley_votes})
    \n ------------------------------------------------
    \n Winning Candidate:  {Winning_Candidate}
    \n ------------------------------------------------
    ''')