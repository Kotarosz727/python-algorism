def select_sort(numbers):
    len_numbers = len(numbers)
    for i in range(0, len_numbers):
        min_idx = i
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers    

numbers = [2,5,1,8,7,3]
select_sort(numbers)
print(select_sort(numbers))