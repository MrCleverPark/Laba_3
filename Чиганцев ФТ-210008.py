ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ'*1000000 #Создание алфавита
eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*10000000 #Создание алфавита
message=input('Введите текст ЗАГЛАВНЫМИ буквами Русского или Английского алфавита: ')
lang=input('Введите язык RU или EU: ')
number=int(input('Введите шаг сдвига '))
d = ''
if lang == 'RU':
    for i in message: # Алгоритм для шифрования сообщения
        place=ru.find(i) #Вычисляем места символов в списке
        new=place+number #Сдвигаем символы на указанный шаг
        if i in ru:
            d+=ru[new] # Задаем итоговое значение
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
