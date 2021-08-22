#https://www.geeksforgeeks.org/find-the-missing-number-in-a-sorted-array/
#time complexity of O(log n) 


# A binary search based program to find
# the only missing number in a sorted
# in a sorted array of distinct elements
# within limited range
def search(ar, size):
    a = 0
    b = size - 1
    mid = 0
    while b > a + 1:
        mid = (a + b) // 2
        if (ar[a] - a) != (ar[mid] - mid):
            b = mid
        elif (ar[b] - b) != (ar[mid] - mid):
            a = mid
    return ar[a] + 1