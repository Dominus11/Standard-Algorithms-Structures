# Sorting

from random import randrange, shuffle

# Bubble Sort

# bubbleSort - Bubble Sort
def bubbleSort(arr: list):
    sorted = False
    checkTo = len(arr)-1

    while not sorted and checkTo > 1:
        # Sets sorted to True so that it can then be reset while going over the list, if in fact two items aren't sorted
        sorted = True 

        for i in range(checkTo):
            if arr[i] > arr[i+1]:
                sorted = False # If this ever happens then we know it isn't yet sorted and we can't break out early on this pass
                arr[i], arr[i+1] = arr[i+1], arr[i] 

        checkTo -= 1 # Optimisation because the highest item will bubble up at the high of each pass

    return arr

# Time Complexity: O(n^2) / O(n)
# Worst/Average case, it has to do multiple passes of the list (n iterations) up to a maximum of n-1 times, giving O(n^2)
# Best case, only n - 1 comparisons have to be made, really really unlikely though, so average is n^2

# Space Complexity: O(1)

# Insertion Sort

# insertionSort - Insertion Sort
def insertionSort(arr: list):
    tempStorage = None
    checkFrom = None 

    for i in range(1,len(arr)):
        tempStorage = arr[i]    # The item being compared
        checkFrom = i - 1         # Pointer to the index whose item we're comparing

        # Ie while the preceding item exists and is greater than the item being compared
        while arr[checkFrom] > tempStorage and checkFrom >= 0:
            arr[checkFrom + 1] = arr[checkFrom]
            checkFrom -= 1

        # Slots the item being compared back into place
        arr[checkFrom+1] = tempStorage

    return


# Time Complexity: O(n^2) / O(n)
# Worst Case: it does 1/2(n^2 - n) comparisons (going from 1 comparison to n comparisons) and 1/2(n^2 - n) shuffles (in average case this gets halved,
# but assuming you have to shuffle all the items every time - ie a reverse order array)
# Best Case: it does (n-1) comparisons and (n-1) shuffles

# Space Complexity: O(1)

# Merge Sort

# merge - Merges two lists, putting them in order
def merge(arr1: list, arr2:list):
    merged = []

    while len(arr1) > 0 and len(arr2) > 0:

        if arr1[0] < arr2[0]:
            merged.append(arr1.pop(0))
        else:
            merged.append(arr2.pop(0))

    # Adds remaining items from either of the two lists. 
    # merged.extend(arr1)
    # merged.extend(arr2) 
    
    return merged

# mergeSort - Merge Sort (recursive)
def mergeSort(arr:list):
    mid = len(arr)//2
    left, right = arr[mid:], arr[:mid]
    # Keeps splitting both sides into lists until they're eventually size 1
    left = mergeSort(left) if len(left) > 1 else left
    right = mergeSort(right) if len(right) > 1 else right

    return merge(left, right)

# Time Complexity : O(nlogn) - Never a distinction as it always has to keep breaking the list down and building it back up
# Space Complexity: O(n) - We must create arrays of size n/2^k with each kth recursion

# mergeSortSentinel - Cambridge optimised version of merge sort
def mergeSortSentinel(arr: list):
    if len(arr) == 1:
        return arr
    
    # Divide
    leftHalf = arr[:len(arr)//2]
    rightHalf = arr[len(arr)//2:]

    # Conquer
    sortedLeft = mergeSortSentinel(leftHalf)
    sortedRight = mergeSortSentinel(rightHalf)
    
    # Combine

    # Adding these sentinels means that when one list reaches infinity the items in the other will always be less
    # Hence it'll keep pouring out of the other list until both point to infinity
    sortedLeft.append(float('inf'))
    sortedRight.append(float('inf'))

    lIdx,rIdx= 0,0
   
    for mergedIdx in range(0,len(arr)):
        if sortedLeft[lIdx] < sortedRight[rIdx]:
            arr[mergedIdx] = sortedLeft[lIdx]
            lIdx += 1
        else:
            arr[mergedIdx] = sortedRight[rIdx]
            rIdx += 1

    return arr

# Quick Sort

# partition - Splits up the list and reorders it. Pivot will be rightmost element
def partition(arr: list, startIdx: int, endIdx: int, pivotIdx: int):
    if len(arr) < 2:
        return arr
    
    # Move pivot to start of array
    pivotValue = arr[pivotIdx]
    arr[startIdx], arr[pivotIdx] = arr[pivotIdx], arr[startIdx]

    # Set high and low pointers
    # On each iteration increment high, check to see if the value should be in the region
    #   If it should be in the higher region, swap the value at low and high, increment low to exclude this one now
    #   Otherwise carry on

    low = startIdx + 1
    for high in range(startIdx + 1, endIdx + 1):
        if arr[high] < pivotValue:
            arr[high], arr[low] = arr[low], arr[high]
            low += 1
    
    # Put pivot value back into place
    arr[startIdx], arr[low - 1] = arr[low - 1], arr[startIdx]

    # Return pivot index
    return low -1



# quickSort - Recursive Quick Sort algorithm
def quickSort(arr: list, startIdx:int = None, endIdx:int = None):
    startIdx = 0 if startIdx == None else startIdx
    endIdx = len(arr)-1 if endIdx == None else endIdx

    if len(arr) < 2:
        return arr

    if startIdx > endIdx:
        return 

    # Divide
    pivotIdx = randrange(startIdx, endIdx +1)
    pivotIdx = partition(arr,startIdx,endIdx, pivotIdx)

    # Conquer and combine
    quickSort(arr,startIdx,pivotIdx-1)
    quickSort(arr,pivotIdx+1,endIdx)

    return 

# Tine Complexity: O(n^2)/ O(nlogn) 
# Worst Case: Pivot being start element - moving 'high' 1/2(n^2 - n) times 
# Best Case: Pivot being median element - only having log_2(n) levels to work on

# Space Complexity: O(1)

# Insecure - If you use Quicksort you can get DoSed, as they can keep supplying worst case data to your servers, changing the time complexity of quicksort 
#            from linearithmic to quadratic, hence using a random pivot prevents this as no malicious attackers can anticipate this. 
# Unstable - The relative order of identically valued items before sorting is not maintained in the sorted list.



def main():
    arr = [i for i in range(10)]
    shuffle(arr)
    quickSort(arr)
    print(arr)

main()

