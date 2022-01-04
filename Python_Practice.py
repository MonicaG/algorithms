# Python practice

# Q1:
# Create a dictionary from the list: arr = [1, 2, 3, 4, 5, 3, 7, 2]
# where the keys are the element and the values is a list of index positions

#Q2:
# Given the list: some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# Use a set to find duplicates












#---------------- Answers -------------------------------

#Q1
from collections import defaultdict
arr = [1, 2, 3, 4, 5, 3, 7, 2]
cache = defaultdict(list)
for i in range(len(arr)):
    cache[arr[i]].append(i)

print(cache)

#Q2
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)