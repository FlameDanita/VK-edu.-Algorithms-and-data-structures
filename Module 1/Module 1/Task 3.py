# Реализовать сортировку вставками (insertion sort)
# На вход подаётся массив чисел
# На выходе ожидается отсортированный массив чисел

# n = int(input())
# nums = input().split()
nums = '12 11 13 5 6 5 1 3 4'.split()
# nums = list(map(lambda x: int(x) , nums))
nums = [int(x) for x in nums]

def insert_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while (j >= 0 and temp < nums[j]):
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = temp

        print(nums)

    return nums
 
print(*insert_sort(nums))