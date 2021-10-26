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

def gen_rand_numb(list_length):
    '''
    Returns a list of unsorted integers.

    Parameters:
        list_length (int): The length of the list to be generated.

    Returns:
        randomlist (list): List of integers (unsorted).
    '''

    randomlist = []

    for num in range(list_length):
        randomlist.append(random.randint(1,list_length))

    return(randomlist)

# ------------- Define Sorting Algorithms ------------
def bublesort(arr):
    '''
    Returns a sorted list of a given list by using bubble sorting.

    Parameters:
        arr (list): List to be sorted.

    Returns:
        arr (list): List that has been sorted.
    '''

    swap_happened = True

    while swap_happened:
        swap_happened = False

        for num in range(len(arr) - 1):

                if(arr[num] > arr[num+1]):
                    swap_happened = True
                    arr[num], arr[num+1] = arr[num+1], arr[num]

    return arr

def insertionsort(arr):
    '''
    Returns a sorted list of a given list by using insertion sorting.

    Parameters:
        arr (list): List to be sorted.

    Returns:
        arr (list): List that has been sorted.
    '''

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

def selectionsort(arr):
    '''
    Returns a sorted list of a given list by using selection sorting.

    Parameters:
        arr (list): List to be sorted.

    Returns:
        arr (list): List that has been sorted.
    '''
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
    '''
    Returns a sorted list of a given list by using merge sorting.

    Parameters:
        arr (list): List to be sorted.

    Returns:
        arr (list): List that has been sorted.
    '''

    return(divide_arr(arr))

def quicksort(arr):
    '''
    Returns a sorted list of a given list by using quick sorting.

    Parameters:
        arr (list): List to be sorted.

    Returns:
        arr (list): List that has been sorted.
    '''

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
    
def builtinsort(arr):
    '''
    Returns a sorted list of a given list by using built-in (tim-sort) sorting.

    Parameters:
        arr (list): List to be sorted.

    Returns:
        arr (list): List that has been sorted.
    '''

    arr.sort()

    return arr

def algo_analyzer(func_name, list):
    '''
    Returns a sorted list of a given list by using built-in (tim-sort) sorting.
    Prints out the name of sorting algorithm and time it takes to sort a given
    array. 

    Parameters:
        func_name (str): Name of the sorting algorithm.
        list (list): List to be sorted.

    Returns:
        sorted_arr (list): List that is sorted.
    '''

    start_time = time.time()

    sorted_arr = func_name(list)

    end_time = time.time()
    time_elapsed = 0.0
    time_elapsed = round(end_time - start_time, 3)
 
    print(f"{func_name.__name__.capitalize()[:-4]} Sort\t took {time_elapsed} seconds")

    return sorted_arr

def run_analyzer():
    '''
    Generate a list of random numbers, and sort it by using sorting algorithms.
    At the end, return lists from each sorting algorithm execution.

    Parameters:

    Returns:
        bubble_sorted_arr (list): Sorted list via bubble sort.  
        insertion_sorted_arr (list): Sorted list via insertion sort.
        selection_sorted_arr (list): Sorted list via selection sort.
        merge_sorted_arr (list): Sorted list via merge sort.
        quick_sorted_arr (list): Sorted list via quick sort.
        builtin_sorted_arr (list): Sorted list via built-in sort.
    '''

    # create unsorted array.  
    unsorted_arr = gen_rand_numb(size_of_list) 
    
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
