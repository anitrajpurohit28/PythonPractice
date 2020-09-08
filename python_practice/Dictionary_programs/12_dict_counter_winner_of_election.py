# 12 Dictionary and counter in Python to find winner of election
from collections import Counter
input1 = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie',
          'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']


def election_winner1(input):
    vote_dict = Counter(input)
    # print(vote_dict)
    # here we are using both key x[1] and x[0] to sort the order.
    # If only x[1] is used, values will be sorted only by values
    # with both x[1] and x[0], values will be sorted based on x[1] if values clash,
    # it'll match based on x[0] then
    value_sorted = sorted(vote_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
    print(value_sorted)
    print(value_sorted[0][0])
    # print(f"Winner: {value_sorted[value_sorted[1]]}")


election_winner1(input1)

print(" ---- using Counters and max ----")

from collections import Counter

vote_dict = Counter(input1)
max_votes = max(vote_dict.values())
max_vote_list = [i for i in vote_dict.keys() if vote_dict[i] == max_votes]
print(max_vote_list)
print(sorted(max_vote_list)[0])
