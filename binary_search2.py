from typing import List

def binari_search(num: List, target: int) -> int:
    def _binary_search(num:List, target:int, left:int, right:int) ->int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            return _binary_search(num, target, mid + 1, right)
        else:
            return _binary_search(num, target, left, mid -1)

    return _binary_search(num, target, 0, len(num)-1)    

num = [0,1,5,7,9,11,15,20,24]
target = 5
res = binari_search(num, target)
print(res)
