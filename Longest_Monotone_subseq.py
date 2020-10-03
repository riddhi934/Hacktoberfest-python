def answer(arr):
    n = len(arr)
    index = [1 for i in range(n)]
    for j in range(1,n):
        for k in range(0,j):
            if arr[j] > arr[k] and index[j] < index[k] + 1:
                index[j] = index[k] + 1
    maxi = 0
    for d in range(n):
        maxi = max(maxi,index[d])
    return maxi

arr = list(map(int,input().split()))
print(answer(arr))