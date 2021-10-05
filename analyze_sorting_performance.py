import time
import random

# Get inputs from user
size_of_list = int(input("What size of the list you want to create? "))

bubble_sorted_arr       = []
insertion_sorted_arr    = []
selection_sorted_arr    = []
merge_sorted_arr        = []
quick_sorted_arr        = []
builtin_sorted_arr      = []

# Generate unsorted list to be sorted.
def gen_rand_numb(list_length, list_range):
    randomlist = []
    for num in range(list_length):
        randomlist.append(random.randint(1,list_range))
    return(randomlist)

# ------------- Define Sorting Algorithms ------------
# Define bubble sort.
def bubblesort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr) - 1):
                if(arr[num] > arr[num+1]):
                    swap_happened = True
                    arr[num], arr[num+1] = arr[num+1], arr[num]
    return arr

# Define insertion sort.
def insertionsort(arr):
    key_index = 1
    for key_index in range(1, len(arr)):
        comp_index = key_index - 1
        while comp_index >= 0:
            if arr[key_index] < arr[comp_index]:
                arr[key_index], arr[comp_index] = arr[comp_index], arr[key_index]
                key_index = comp_index
                comp_index -= 1
            else:
                break
    return arr

# Define Selection Sort.
def selectionsort(arr):
    for elem in range (len(arr)-1):
        for num in range (elem + 1, len(arr)):
            if(arr[elem] > arr[num]):
                arr[elem], arr[num] = arr[num], arr[elem]
    return arr

# Define Merge Sort. 
def conquer(arr1,arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def divide_arr(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return conquer(l1, l2)

def mergesort(arr):
    return(divide_arr(arr))

# Define Quick Sort
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr)//2]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)
    
# Python built-in Sort
def builtinsort(arr):
    arr.sort()
    return arr

def algo_analyzer(func_name, list):
    start_time = time.time()

    sorted_arr = func_name(list)

    end_time = time.time()
    time_elapsed = 0.0
    time_elapsed = round(end_time - start_time, 3)
 
    print(f"{func_name.__name__.capitalize()[:-4]} Sort\t took {time_elapsed} seconds")

    return sorted_arr

def run_analyzer():
    # create unsorted array.  
    unsorted_arr = gen_rand_numb(size_of_list, size_of_list) 
    
    # Print seperater with 40 times dashes.
    print("-" * 40)
    
    # Run algo analyzer for every sorting algo. Insert copy of unsorted_arr
    # each time since we sort arrays in place.
    bubble_sorted_arr       = algo_analyzer(bubblesort, unsorted_arr.copy())
    insertion_sorted_arr    = algo_analyzer(insertionsort, unsorted_arr.copy())
    selection_sorted_arr    = algo_analyzer(selectionsort, unsorted_arr.copy())
    merge_sorted_arr        = algo_analyzer(mergesort, unsorted_arr.copy())
    quick_sorted_arr        = algo_analyzer(quicksort, unsorted_arr.copy())
    builtin_sorted_arr      = algo_analyzer(builtinsort, unsorted_arr.copy()) 

    # Print seperater with 40 times dashes.
    print("-" * 40)

    return(bubble_sorted_arr, insertion_sorted_arr, selection_sorted_arr,
            merge_sorted_arr, quick_sorted_arr, builtin_sorted_arr)

if __name__ == "__main__": 
    run_analyzer()
