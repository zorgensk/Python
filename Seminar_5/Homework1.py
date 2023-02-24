# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def correct_text(text, st):
    new_text = [str(i) for i in text.split()  if 'абв' not in i]
    return ' '.join(new_text)

text = "Шпионы абвера высадились в Зимбабве"
print(correct_text(text, 'абв'))
