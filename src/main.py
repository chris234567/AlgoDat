from datetime import datetime
from utils import generate_random_array
from sorting_algorithms.insertion_sort import sort, BIG_O

a = generate_random_array(100)

# print("----unsorted array----")
# print(a)

t1 = datetime.now()
sorted = sort(a)
t2 = datetime.now()

# print("\n-----sorted array-----")
# print(sorted)

print("\nTime complexity for insertion sort is {}.".format(BIG_O))
print("The runtime is {} seconds.".format(str((t2 - t1))[5:]))