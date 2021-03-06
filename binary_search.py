from typing import List

def binari_search(num: List, target: int) -> int:
    left, right = 0, len(num)-1
        
    while left <= right:
        mid = (left + right) // 2
        if num[mid] == target:
            return mid
        elif num[mid] < target:
           left =  mid + 1
        else:
            right = mid -1

num = [0,1,5,7,9,11,15,20,24]
target = 5
res = binari_search(num, target)
print(res)
