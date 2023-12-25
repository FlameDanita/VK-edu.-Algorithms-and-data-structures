'''
Вам нужно написать программу, которая сортирует все книги по году издания в порядке возрастания.
Если две или более книг были изданы в один и тот же год, сортируйте их по названию в алфавитном
порядке. Используйте сортировку слиянием для решения этой задачи.
'''

n = int(input())
# n = 3

books_dict = {}
for i in range(n):
    # books_arr.append(input().split())
    tmp = input()
    books_dict[int(tmp[:10])] = [tmp[11:-5], int(tmp[-4:])]

# tmp = '1234567890 "Война и мир" 1869'
# books_dict[int(tmp[:10])] = [tmp[11:-5], int(tmp[-4:])]

# tmp = '9876543210 "1984" 1949'
# books_dict[int(tmp[:10])] = [tmp[11:-5], int(tmp[-4:])]

# tmp = '1111111111 "Сказка о рыбаке и рыбке" 1833'
# books_dict[int(tmp[:10])] = [tmp[11:-5], int(tmp[-4:])]

# print(books_dict)

sorted_dict = {k: v for k, v in sorted(books_dict.items(), key=lambda item: item[1][1])}

# print(sorted_dict)

for k, v in sorted_dict.items():
    print(k, *v)