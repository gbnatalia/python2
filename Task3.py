'''
3.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
o	x=34; y=-30 -> 4
o	x=2; y=4-> 1
o	x=-34; y=-30 -> 3
'''

def num_segment(x, y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 2
    else:
        if y > 0:
            return 4
        else:
            return 3


if __name__ == "__main__":

    cont = 'y'

    while cont == 'y':
        try:
            x = int(input("Введите координату x: "))
            y = int(input("Введите координату y: "))
            print("Номер сегмента: ", num_segment(x, y))
        except ValueError:
            print("Введено не число!")

        cont = input('Хотите еще попробовать (y - да, иначе нет):')

