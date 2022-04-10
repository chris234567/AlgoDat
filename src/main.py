from datetime import datetime
from utils import generate_random_array

from sorting_algorithms.insertion_sort import sort as insertion_sort, BIG_O
from sorting_algorithms.merge_sort import sort as merge_sort
from sorting_algorithms.quick_sort import sort as quick_sort

a = generate_random_array(10)

# # print("----unsorted array----")
# # print(a)

# t1 = datetime.now()
# sorted = insertion_sort(a)
# t2 = datetime.now()

# # print("\n-----sorted array-----")
# # print(sorted)

# print("\nTime complexity for insertion sort is {}.".format(BIG_O))
# print("The runtime is {} seconds.".format(str((t2 - t1))[5:]))

#print(merge_sort(a))

print(quick_sort(a, 0, len(a) - 1))
