'''
WAP to count the total votes and print the output in the form of a dictionary where
the key is the candidate name and value is the total number of votes in the order
of maximum votes.
    write function for voting
        • vote takes a single argument, a string called name, representing the name of
        the candidate who was voted for.
        • If the name matches one of the names of the candidates in the election, then
        update that candidate’s vote total to account for the new vote. The vote
        function in this case should return true to indicate a successful ballot.
        • If name does not match the name of any of the candidates in the election, no
        vote totals should change, and the vote function should return false to
        indicate an invalid ballot.

        • You may assume that no two candidates will have the same name.
    Write a print_winner function.
        • The function should print out the name of the candidate who received the
        most votes in the election, and then print a newline.
        • It is possible that the election could end in a tie if multiple candidates each
        have the maximum number of votes. In that case, you should output the
        names of each of the winning candidates, each on a separate line.
    '''

def vote(name):
    if name in candidates:
        if name not in vote_count:
            vote_count[name] = 1

        vote_count[name] += 1

        return True
    
    else:
        return False

def print_winner(vote_count):
    
    max_vote = max(vote_count.values())
    winners = [name for name, value in vote_count.items() if value == max_vote]

    print("Winner(s) of the election:\n")
    for name in winners:
        print(name)

vote_count = {}

candidates = ['Modi', 'Rahul', 'Yogi', 'Amitshah', 'Nirmala', 'Priyanka']


vote('Modi')
vote('Rahul')
vote('Yogi')
vote('Modi')
vote('Modi')
vote('Rahul')
vote('Nirmala')
vote('Rahul')
print(vote('Sharukh'))

print_winner(vote_count)