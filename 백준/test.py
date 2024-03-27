from itertools import permutations

arr = [i for i in range(1, 4)]
for v in permutations(arr, 3):
    print(v)
