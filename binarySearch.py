#Taking User Input

N=int(input())
arr=list(map(int,input().split()))
K=int(input())

#Binary Search Function

def binarysearch():
    for i in range(len(arr)):
        if arr[i]==K:
            print(i)

#Giving Output

binarysearch()
