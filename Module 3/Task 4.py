'''
Дано бинарное дерево поиска в виде массива.
Необходимо написать функцию, которая находит и возвращает минимальный элемент в дереве
'''

n = int(input())
# n = 11

tree = input().split()
# tree = '16 11 18 9 13 17 21 7 10 12 15'.split()

work_nums = []
for num in tree:
    work_nums.append(int(num))

print(max(work_nums))