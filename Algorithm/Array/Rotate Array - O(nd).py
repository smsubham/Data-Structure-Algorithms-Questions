#https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
# Time complexity : O(n * d), Auxiliary Space : O(1)

T = int(input())
for i in range(int(T)):
    N,D = input().split()
    N = int(N)
    k = int(D)
    arr = input().split()
    while k>0:
        arr.append(arr[0])
        arr.remove(arr[0])
        k-=1
    print(' '.join(arr))