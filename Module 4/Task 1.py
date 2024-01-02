'''
У вас есть граф, где каждая вершина представляет человека, а ребро между двумя вершинами означает, что эти два человека друзья.
Найдите, существуют ли три человека, которые все взаимно дружат друг с другом (то есть между каждой парой из трех человек существует ребро).
'''

# n = 3
# d = {
#     1: [2, 3],
#     2: [1],
#     3: [1]
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

flag = False
for values in d.values():
    for i in range(len(values)):
        for j in range(len(values)):
            if i != j and values[j] in d[values[i]]:
                # print(values[j], 'in key =', values[i] ,d[values[i]])
                flag = True
                break
            

if flag:
    print('YES')
else:
    print('NO')
