def task1():
    # Напишите программу, которая принимает на вход вещественное число 
    # и показывает сумму его цифр.

    num = float(input("Введите число: "))
    num_string = str(num)
    num_string = num_string.replace('.', '')
    string_list = list(num_string)
    num_list = map(int, string_list)
    my_sum = sum(num_list)
    print(f'Сумма цифр равна: {my_sum}')

def task2():
    # Напишите программу, которая принимает на вход число N 
    # и выдает набор произведений чисел от 1 до N.

    num = int(input("Введите число: "))
    mult = 1
    for i in range(1, num + 1):
        mult *= i
        print(mult, end = ' ')
        i += 1

def task3():
    # Задайте список из n чисел заполненный по формуле (1 + 1 / n) ** n 
    # и выведите на экран их сумму.

    num = int(input("Введите число: "))
    my_dict = dict()
    for i in range(1, num + 1):
        my_dict[i] = round((1 + 1 / i) ** i)
    print(f'Список из {num} чисел : {my_dict}. Сумма чисел из списка: {sum(my_dict.values())}')

def task4():
    # Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
    # Найдите произведение элементов на указанных позициях(не индексах). 
    # Позиции хранятся в файле file.txt, в одной строке одно число.

    interval = int(input("Введите число: "))
    my_list = list()
    for i in range(-interval, interval + 1):
        my_list.append(i)

    first_pos = int(input("Введите первую позицию: "))
    while first_pos > interval * 2 + 1:
        print('Введено неверное число')
        first_pos = int(input("Введите первую позицию: "))

    second_pos = int(input("Введите вторую позицию: "))
    while second_pos > interval * 2 + 1:
        print('Введено неверное число')
        second_pos = int(input("Введите первую позицию: "))

    path = 'file.txt'
    with open(path, 'w') as data:
        data.write(f'{first_pos}\n')
        data.write(f'{second_pos}\n')

    print(f'Список чисел в промежутке от -{interval} до {interval}]: {my_list}')

    data = open(path, 'r')
    num_first = int(data.readline())
    num_second = int(data.readline())
    mult = my_list[num_first - 1] * my_list[num_second - 1]
    data.close()
    print(f'Произведение чисел на позициях {num_first} и {num_second} = {mult}')

def task5():
    # Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

    from random import sample
    my_list = list()
    my_range = int(input("Введите число: "))
    for i in range(my_range + 1):
        my_list.append(i)
    print('Сформированный список: ', my_list)
    print('Перемешанный список: ', sample(my_list, my_range + 1))



task1()
# task2()
# task3()
# task4()
# task5()