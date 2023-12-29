'''
Есть строка с многократным повторением разных букв.
Надо понять какое максимальное количество повторений встречается в строке.
Используя хеш таблицу, записывайте пару буква - количество вхождений в строку.
'''

def search_max_letter(string):
    d = {}
    for letter in string:
        if letter in d.keys():
            d[letter] += 1
        else:
            d[letter] = 1

    return max(d.values())

string = input()
# string = 'adeuuuuio'

print(search_max_letter(string))