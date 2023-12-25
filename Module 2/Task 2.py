'''
Дана строка s. Строка состоит из английских букв в нижнем
регистре.Необходимо из строки удалить все рядом стоящие
повторяющиеся буквы. Например, в строке xyyx мы должны
удалить yy, а после и оставшиеся xx и того после должна
получиться пустая строка. Или же в строке fqffqzzsd после
удаления остануться только fsd. Первыми удаляться ff,
являющимися третьими и четвертыми символами, затем qq и
после уже zz.
'''

def delete_task2(buf):
    flag = True

    while flag:
        # print((buf))
        flag = False

        for i in range(len(buf) - 1):
            if buf[i] == buf[i + 1]:
                flag = True

                buf = buf[:i] + buf[i+2:]

                break

    return buf

s = input()
# s = 'cdffd'

print(delete_task2(s))