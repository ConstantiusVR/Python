# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара) 

print ('Введите любой текст на русском языке:');
text = input()
new_text = text.split()
selected_text = list(filter(lambda x: False if 'абв' in x.lower() else True, new_text)) 
print (selected_text) 



# 39(1). Создайте программу для игры с конфетами человек против человека. 
# Реализовать игру игрока против игрока в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. 
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил.

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# В качестве дополнительного усложнения можно:
#        a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#        b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить 
#         какое количесвто конфет необходимо брать, чтобы гарантированно победить, 
#         соответственно внедрить этот алгоритм боту )

# РЕШЕНИЕ ДЛЯ ДВУХ ИГРОКОВ: 
print ('Введите имя игрока:');
player1 = input()
print ('Введите имя другого игрока:');
player2 = input() 
playerlist = [player1, player2]
print ('Введите число 1 или 2:');
a = int(input()) 
import random
b = [player2, player1]
c = [player1, player2]
if a==1: 
    result = random.choice(b);
    print ('начинает игрок:',result)
elif a==2:
    result = random.choice(c);
    print('начинает игрок:',result)
else:
    print ('введено неверное число')

first_player = result 
if result == player1:
    second_player = player2
elif result == player2:
    second_player = player1    

print('вторым играет:',second_player)
candies = 221
while candies >= 0:
    print (first_player,'введите число конфет от 1 до 28:');
    first = int(input())
    if 0< first <=28: 
        candies = candies - first 
        print (candies) 
        if candies <=0:
            print (first_player, 'вы победитель!')
            exit()
    elif first >28:
        print ('Вы ввели число превышающее допустимое! Вы пропускаете ход.')
    print (second_player,'введите число конфет от 1 до 28:');
    second = int(input())
    if 0< second <=28:
        candies = candies - second 
        print (candies)
        if candies <=0:
            print (second_player, 'вы победитель!')
            exit()
    elif first >28:
        print ('Вы ввели число превышающее допустимое! Вы пропускаете ход.')
 

# РЕШЕНИЕ ДЛЯ ИГРОКА С БОТОМ:

print ('Введите имя игрока:');
player1 = input()
player2 = 'Bot'

playerlist = [player1, player2]
print ('Введите число 1 или 2:');
a = int(input()) 
import random
b = [player2, player1]
c = [player1, player2]
if a==1: 
    result = random.choice(b);
    print ('начинает игрок:',result)
elif a==2:
    result = random.choice(c);
    print('начинает игрок:',result)
else:
    print ('введено неверное число')

first_player = result 
if result == player1:
    second_player = player2
elif result == player2:
    second_player = player1    

print('вторым играет:',second_player)
candies = 221
if result == player1:
    while candies >= 0:
        print (first_player,'введите число конфет от 1 до 28:');
        first = int(input())
        if 0< first <=28: 
            candies = candies - first 
            print (candies) 
            if candies <=0:
                print (first_player, 'вы победитель!')
                exit()
        elif first >28:
            print ('Вы ввели число превышающее допустимое! Вы пропускаете ход.')
        print ('Бот делает ход')
        second = int 
        if candies >=56:
            if first%2==0 and first<=26:
                second = first+1
                print(second)
                candies = candies - second 
                print (candies)
            elif first%2==1 and first<=28:
                second = first
                print (second)
                candies = candies - second
                print(candies)
        elif candies == 56:
            second = 27
            print(second)
            candies = candies - second
            print(candies)
        elif 28<candies <56:
            import random
            second = random.randint(1, 3)
            print(second)
            candies = candies - second
            print(candies)
        elif candies <=28:
            second = candies
            print(second)
            candies = candies - second
            print(candies)
            print (second_player, 'победитель!')
            exit()
if result == player2:
    while candies >=0:
        print('Бот делает ход')
        first = int
        if candies > 56: 
            if candies%2==0:
                import random
                first = random.randint(1, 28)
                print(first)
                candies = candies - first 
                print (candies)
            elif candies%2==1:
                first = 21
                print(first)
                candies = candies - first
                print(candies)
        elif candies == 56:
                first = 27
                print(first)
                candies = candies - first
                print (candies)
        elif 28< candies < 56:
                import random
                first = random.randint (1, 3)
                print(first)
                candies = candies - first
                print(candies)
        elif candies <=28:
                first = candies
                print(first)
                candies = candies - first
                print(candies)
                print (first_player, 'победитель!')
                exit()
        print (second_player,'введите число конфет от 1 до 28:');
        second = int(input())
        if 0< second <=28: 
            candies = candies - second 
            print (candies) 
            if candies <=0:
                print (second_player, 'вы победитель!')
                exit()
        elif second >28:
            print ('Вы ввели число превышающее допустимое! Вы пропускаете ход.')



# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.


def encoder(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 

    if not data: return '' 

    for char in data: 
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding



def decoder(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 
            return decode
