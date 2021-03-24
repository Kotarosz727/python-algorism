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

def bucket_sort(numbers):
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    buckets = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[i-1].append(num)

    for i in range(size):
        # buckets[i] = insertion_sort(buckets[i])
        insertion_sort(buckets[i])

    res = []
    for i in range(size):
        res += buckets[i]    

    return res

numbers = [1,5,28,25,100,52,27,91,22,99]
res = bucket_sort(numbers)
print(res)