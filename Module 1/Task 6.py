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

    nums = sorted(odd_arr)
    nums.extend(sorted(not_odd_arr))

    return(nums)

print(*booble_sort(nums))