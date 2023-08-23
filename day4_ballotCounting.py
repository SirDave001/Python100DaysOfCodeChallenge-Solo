polls = ['ade', 'ope', 'ade', 'ope', 'ope', 'ola', 'seyi', 'ade', 'ola', 'ade', 'seyi', 'ade', 'ope', 'ope', 'ade', 'ope', 'ade']

candidates = []
votes = []

for person in polls:
    if person not in candidates:
        candidates.append(person)
        votes.append(1)
    else:
        candidates_index = candidates.index(person)
        votes[candidates_index] += 1
max_vote = 0
max_candidates = []
for i in range(len(votes)):
    if votes[i] > max_vote:
        max_vote = votes[i]
        candidate = candidates[i]
        max_candidates = []
        max_candidates.append(candidate)
    elif votes[i] == max_vote:
        candidate = candidates[i]
        max_candidates.append(candidate)
print(f'The highest vote goes to: {max_candidates}')
print(f'each person has {max_vote} votes')