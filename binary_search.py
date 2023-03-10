def binarySearch(arr, low, high, x):
    """
     Binary search for x in arr [ low : high ]. The search is based on binary search and will raise an exception if x is not found.
     
     @param arr - The array to search. Must be sorted.
     @param low - The low bound of the search range. It is assumed that this is greater than or equal to the value x.
     @param high - The high bound of the search range. It is assumed that this is greater than the value x.
     @param x - The value to search for. It is assumed that this is an integer.
     
     @return The index of x or - 1 if x is not in the range. This is a convenience function
    """
    if high >= low:
        mid = (high + low) // 2
    
        if arr[mid] == x:
            return mid
    
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 40

result = binarySearch(arr, 0, len(arr) - 1, x)

if result!= -1:
    print("Element is at index ", str(result))
else:
    print("Element not present")