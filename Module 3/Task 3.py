'''
Дана последовательность целых чисел и число K.
Найдите максимальное произведение подпоследовательности размером K.
'''

# n = int(input())
n = 5

# arr = input().split()
arr = '1 2 -4 3 5'.split()

work_nums = []
for num in arr:
    work_nums.append(int(num))

arr = work_nums

# k = int(input())
k = 2

arr.sort()
print(arr)

res = 1
for i in range(k):
    res *= arr[-1 - i]

print(res)
