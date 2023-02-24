# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def archive_RLE(code):
    result = ''
    next_value = ''
    count = 1
    if not code:
        return ''

    for i in code:
        if i != next_value:
            if next_value:
                result += str(count) + next_value
            count = 1
            next_value = i
        else:
            count += 1
    else:
        result += str(count) + next_value
        return result

def decode_RLE(code):
    decoding = ''
    count = ''
    for char in code:
        if char.isdigit():
            count += char
        elif char.isalpha():
            decoding += int(count) * char
            count = ''
    return decoding



code = input("Введите текст, который нужно заархивировать: ")
code = list(code)


print(archive_RLE(code))

print(decode_RLE(archive_RLE(code)))