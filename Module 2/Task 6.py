'''
На вход функции подается две строки a и b
Используя хеш таблицу, попытайтесь определить, является ли строка b анаграммой к строке a.
Анаграмма – это слово или фраза, образованные путем перестановки букв другого слова или фразы,
как правило, используя все исходные буквы ровно один раз
'''

def search_letter_count(string):
    d = {}
    for letter in string:
        if letter in d.keys():
            d[letter] += 1
        else:
            d[letter] = 1

    return d

intp = input().split()
# intp = "anagram nagaram".split()
a, b = intp[0], intp[1]
# print(a, b)

if search_letter_count(a) == search_letter_count(b):
    print("true")
else:
    print("false")