from datetime import datetime
from utils import generate_random_array

from sorting_algorithms.insertion_sort import sort as insertion_sort
from sorting_algorithms.merge_sort import sort as merge_sort
from sorting_algorithms.quick_sort import sort as quick_sort
from sorting_algorithms.heap_sort import sort as heap_sort

a = generate_random_array(10)

# # print("----unsorted array----")
# # print(a)

# t1 = datetime.now()
# sorted = insertion_sort(a)
# t2 = datetime.now()

# # print("\n-----sorted array-----")
# # print(sorted)

#print(merge_sort(a))

#print(quick_sort(a, 0, len(a) - 1))

print(heap_sort(a))
