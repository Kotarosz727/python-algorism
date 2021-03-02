def merge_sort(num):
    leng = len(num)
    if leng <= 1:
        return num

    center = len(num)//2
    left = num[:center]
    right = num[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            num[k] = left[i]
            i += 1 
        else:
            num[k] = right[j]
            j += 1
        k += 1    

    while i < len(left):
        num[k] = left[i]
        i += 1
        k += 1    

    while j < len(right):
        num[k] = right[j]
        j += 1
        k += 1    

    return num    

import random
num = [5,4,1,8,7,3,2,9]
# num = [random.randint(0, 10000000) for _ in range(10)]
print(merge_sort(num))    