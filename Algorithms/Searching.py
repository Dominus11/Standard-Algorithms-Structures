# Searching

# Linear Search 

def linearSearch(arr: list, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return None

# Time Complexity: O(n)
# Space Complexity: O(1)


# Binary Search

# binarySearch - Recursive binary search
def binarySearch(arr:list, target, low, high):
    if low > high:
        return -5

    mid = (high+low)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearch(arr, target, low, mid-1)
    else:
        return binarySearch(arr, target, mid+1, high)

# binarySearchIter - Iterative binary search
def binarySearchIter(arr: list, target):
    low,high = 0,len(arr)-1
    mid = (low+high)//2

    while low < high:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low,high = 0, mid-1
        else:
            low,high = mid+1,high
    
    return -1

# Time Complexity: O(log_2 n)
# Space Complexity:
#   Iterative: O(1)
#   Recursive: O(log_2 n)
