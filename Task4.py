'''
4.	Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
'''

def get_range(sector_num):
    if sector_num == 1:
        return "x = (0:+∞], y = (0:+∞]"
    elif sector_num == 2:
        return "x = (0:+∞], y = [-∞:0)"
    elif sector_num == 3:
        return "x = [-∞:0), y = [-∞:0)"
    else:
        return "x = [-∞:0), y =  (0:+∞]"


if __name__ == "__main__":
    sector_num = input("Введите номер сектора: ")
    if sector_num != "1" and sector_num != "2" and sector_num != "3" and sector_num != "4":
        print(f"Введено недопустимое значение сектора - {sector_num}")
    else:
        print(get_range(int(sector_num)))