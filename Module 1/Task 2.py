# В школе прошел экзамен по математике. Несколько человек списали решения и были замечены.
# Этим школьникам поставил 0 баллов. Задача: есть массив с оценками, среди которых есть 0.
# Необходимо все оценки, равные нулю перенести в конец массива, чтобы все такие школьники
# оказались в конце списка.

n = int(input())
# n = 9

nums = input().split()
# nums = '0 33 57 88 60 0 0 80 99'.split()
nums = list(map(lambda x: int(x) , nums))

new_arr = []
count = 0
for elem in nums:
    if elem != 0:
        new_arr.append(elem)
    else:
        count += 1

for _ in range(count):
    new_arr.append(0)

print(*new_arr)