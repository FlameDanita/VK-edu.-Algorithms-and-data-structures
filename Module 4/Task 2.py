'''
Определите количество различных социальных кругов в графе.
Социальный круг – это подграф, где все вершины связаны между собой напрямую или через других членов круга.
'''

# n = 4
# d = {
#     1: [2],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [6],
#     6: [5]
# }

n = int(input())
d = {}

for _ in range(n):
    inp = input().split()
    work_arr = []
    for num in inp:
        work_arr.append(int(num))

    if work_arr[0] in d.keys():
        d[work_arr[0]].append(work_arr[1])
    else:
        d[work_arr[0]] = [work_arr[1]]
    
    if work_arr[1] in d.keys():
        d[work_arr[1]].append(work_arr[0])
    else:
        d[work_arr[1]] = [work_arr[0]]

# print(d)

count = 0
for values in d.values():
    if len(values) == 1:
        count += 1

print(int(count/2))
