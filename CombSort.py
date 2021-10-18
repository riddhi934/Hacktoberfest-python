def combsort(num):
    gap = len(num)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(num) - gap):
            j = i+gap
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
                swaps = True
 
num_list = [75, 16, 55, 19, 48, 14, 2, 61, 22, 100]
print("Before: ", num_list)
combsort(num_list)
print("After:  ", num_list)
