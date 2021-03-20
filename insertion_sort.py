def insertion_sort(numbers):
    len_numbers = len(numbers)
    
    for i in range(1, len_numbers):
        tmp = numbers[i]
        j = i-1

        while j >= 0 and numbers[j] > tmp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = tmp   
    return numbers     

numbers = [1,7,3,2,8,5]
res = insertion_sort(numbers)
print(res)