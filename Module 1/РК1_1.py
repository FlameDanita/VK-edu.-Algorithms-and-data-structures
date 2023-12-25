'''
Дан не отсортированный массив целых чисел. Необходимо перенести в начало массива все
четные числа, сохраняя их очередность. То есть если 8 стояла после 6, то после переноса
в начало, он по-прежнему должна стоять после 6
'''

nums = input().split()
# nums = '3 2 4 1 11 8 9'.split()
# nums = list(map(lambda x: int(x) , nums))
nums = [int(x) for x in nums]

def booble_sort(nums):
    odd_arr, not_odd_arr = [], []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            odd_arr.append(nums[i])
        else:
            not_odd_arr.append(nums[i])

    nums = odd_arr
    nums.extend(not_odd_arr)

    return(nums)

def move_even_numbers_to_start(arr):
    # Создаем новый массив для сохранения четных чисел
    result = []
    
    # Перебираем исходный массив
    for num in arr:
        # Если число четное, добавляем его в начало результата
        if num % 2 == 0:
            result.insert(0, num)
    
    # Добавляем все остальные числа (нечетные) в конец результата
    for num in arr:
        if num % 2 != 0:
            result.append(num)
    
    return result

# print(*booble_sort(nums))
# res = booble_sort(nums)
res = move_even_numbers_to_start(nums)
# print(*res)
for r in res:
    print(r)