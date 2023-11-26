# На вход подается не отсортированный массив целых чисел и некоторое целое число «element».
# Необходимо написать функцию, которая вернет количество элементов, которые не равны данному числу «element».
# Возвращаемое значение после работы функции обозначает количество чисел не равные «element».

n = int(input())
# n = 9

nums = input().split()
# nums = '7 8 1 3 11 3 9 4 3'.split()

# nums = []
# for _ in range(n):
#     nums.append(int(input()))

nums = list(map(lambda x: int(x) , nums))
if len(nums) != n:
    element = nums[n]
    nums = nums[:n]
else:
    element = int(input())
# print(nums)

count = 0
for num in nums:
    if num != element:
        count += 1

print(count)
