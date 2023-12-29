'''

1. поиск Фибоначи
2. log(i)
3. Тернаярный и Экспоненциальный
4. Деление на три части

'''

'''
Дан отсортированный по возрастанию массив целых чисел и заданное число.
Заданное число может и не находиться в массиве. Тогда необходимо вернуть предполагаемый индекс,
где мог бы находится элемент. Другими словами, найдите правильное место для вставки элемента.
Если же число есть, то возвращаем его индекс.
'''

def search_insert_index(arr, value):
    for i in range(len(arr)):
        if arr[i] >= value:
            return i

n = int(input())
# n = 5

nums = input().split()
# nums = '5 7 9 11 13'.split()

work_nums = []
for num in nums:
    work_nums.append(int(num))

# print(work_nums)

search_num = int(input())
# search_num = 6

print(search_insert_index(work_nums, search_num))