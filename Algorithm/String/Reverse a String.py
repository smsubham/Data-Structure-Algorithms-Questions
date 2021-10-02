#https://practice.geeksforgeeks.org/problems/reverse-a-string/1


#User function Template for python3

def reverseWord(s):
    #your code here
    s1 = list(s)
    left,right = 0, len(s1)-1
    while left<right:
        s1[left],s1[right] = s1[right],s1[left]
        left += 1
        right -= 1
    return ''.join(s1)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends