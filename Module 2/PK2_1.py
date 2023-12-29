'''
Дан массив целых чисел.
Необходимо вернуть элемент, который встречается больше половины раз.
Если такого элемента нет, возвращайте -1
'''

def search_number_count(string):
    d = {}
    for letter in string:
        if letter in d.keys():
            d[letter] += 1
        else:
            d[letter] = 1

    return d

n = int(input())
# n = 7

nums = input().split()
# nums = '7 7 8 8 8 7'.split()

work_nums = []
for num in nums:
    work_nums.append(int(num))

res = search_number_count(nums)

flag = True
for key, value in res.items():
    if value > len(nums)/2 and flag:
        print(key)
        flag = False

if flag:
    print(-1)