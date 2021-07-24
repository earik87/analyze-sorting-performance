import time
import random

# ------------- Get inputs from user
size_of_list = int(input("What size of the list you want to create? "))
run_time = int(input("How many times you want to run? "))

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

# Define Selection Sort.
def selectionsort(arr):
    for elem in range (len(arr)-1):
        for num in range (elem + 1, len(arr)):
            if(arr[elem] > arr[num]):
                arr[elem], arr[num] = arr[num], arr[elem]

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
    divide_arr(arr)

# Define Quick Sort
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)

def algo_analyzer(func_name, list):
    start_time = time.time()
    if func_name == "sort":
        list.sort()
    else:
        func_name(list)
    end_time = time.time()
    time_elapsed = 0.0
    time_elapsed = round(end_time - start_time,3)
    if func_name =="sort":
        print(f"Built-in sort\t took {time_elapsed} seconds")
    else:
        print(f"{func_name.__name__.capitalize()}\t took {time_elapsed} seconds")

def run_analyzer():
    for run in range(run_time):
        # we need to re-create lists everytime we run the for loop, since they are bein sorted.
        arr = gen_rand_numb(size_of_list, size_of_list) # this is a generate list + used in bubble sort. 
        arr1 = arr.copy() # input for insertion sort.
        arr2 = arr.copy() # input for selection sort.
        arr3 = arr.copy() # input for merge sort.
        arr4 = arr.copy() # input for quick sort.
        arr5 = arr.copy() # input for built-in sort.

        print(f"Run: {run + 1} ")

        algo_analyzer(bubblesort, arr)
        algo_analyzer(insertionsort, arr1)
        algo_analyzer(selectionsort, arr2)
        algo_analyzer(mergesort, arr3)
        algo_analyzer(quicksort, arr4)
        algo_analyzer("sort", arr5) # Built-in python sort.
        
        print("-" * 40)

if __name__ == "__main__":
    run_analyzer()

