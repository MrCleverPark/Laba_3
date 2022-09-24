ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ'
eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
message=input('Введите текст заглавными буквами Русского или Английского алфавита: ')
lang=input('Введите язык RU или EU: ')
number=int(input('Введите число на которое будет сдвигаться буква: '))
d = ''
if lang == 'RU':
    for i in message:
        place=ru.find(i) 
        new=place+number
        if i in ru:
            d+=ru[new]
        else:
            d+=i
else:
    for i in message:
        place=eu.find(i) 
        new=place+number
        if i in eu:
            d+=eu[new]
        else:
            d+=i
print(d)