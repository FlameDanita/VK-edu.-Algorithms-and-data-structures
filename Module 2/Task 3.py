'''
Есть список товаров в магазине отсортированный по возрастанию, необходимо понять,
есть ли в этом списке товар с заданной ценой.
В случае если цена найдена возвращайте true
'''

def search_num(nums, search_nums):
    flag = 'false'

    for num in nums:
        if num == search_nums:
            flag = 'true'

    return flag

n = int(input())
# n = 12

nums = input().split()
# nums = '100 450 730 800 950 999 1000 3000 3300 8000 9990 10000'.split()

work_nums = []
for num in nums:
    work_nums.append(int(num))

# print(work_nums)

search_nums = int(input())
# search_nums = 999

print(search_num(work_nums, search_nums))