'''
Дан массив не отсортированных целых чисел. Написать функцию, которая вернет первое
с конца четное число. При написании кода используйте принцип стека. Если массив не
содержит четного числа возвращать -1.
'''

# n = int(input())
n = 5
nums = input().split()
# nums = ''.split()
# nums = list(map(lambda x: int(x) , nums))
nums = [int(x) for x in nums]

def search_task1(nums):
    res = -1
    while nums:
        tmp = nums.pop()
        if tmp % 2 == 0:
            res = tmp
            break

    return res


if n != 0:
    print(search_task1(nums))
