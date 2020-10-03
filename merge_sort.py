# Merge Sort

def merge(left, right):
    if len(left) == 0:
        return right
        
    if len(right) == 0:
        return left
        
    result = []
    i_left = i_right = 0
    
    while len(result) < len(left) + len(right):
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
            
        if i_right == len(right):
            result += left[i_left:]
            break
            
        if i_left == len(left):
            result += right[i_right:]
            break
            
    return result

def merge_sort(array):
    if len(array) < 2:
        return array
        
    mid = len(array) // 2
    
    return merge(left=merge_sort(array[:mid]), right=merge_sort(array[mid:]))

# print(merge_sort([1,5,3,2,4]))
