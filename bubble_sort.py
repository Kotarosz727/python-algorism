def bubble_sort(numbers):
    len_numbers = len(numbers)
    while len_numbers > 1:
        len_numbers -= 1       
        for i in range(0, len_numbers):
            if numbers[i] > numbers[i+1]:
                numbers[i] , numbers[i+1] = numbers[i+1], numbers[i]

    return numbers    

# numbers = [2,5,1,8,7,4,3]
# res = bubble_sort(numbers)
# print(res)
import random
numbers = [random.randint(0, 1000) for i in range(10)]
res = bubble_sort(numbers)
print(res)