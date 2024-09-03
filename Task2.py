# TASK2

import math


# ФУНКЦИЯ ПО ПРЕОБРАЗОВАНИЮ ИЗ ДЕСЯТИЧНОЙ СИСТЕМЫ СЧИСЛЕНИЯ В ШЕСТНАДЦАТИРИЧНУЮ
def hex_func(number, hex_nums):

    arr_div_num = []

    while number != 0:
        num_dev = number % 16
        number = math.floor(number / 16)
        arr_div_num.append(num_dev)

    arr_div_num.reverse()  # ИСПОЛЬЗУЕМ МЕТОД ПО РАЗВОРОТУ ЧИСЛА


    print("Reverse hex - ", arr_div_num)


    hex_num = ""

    # ОБРАБОТКА ПОЛУЧЕННОГО МАССИВА ЧИСЕЛ И ДАЛЬНЕЙШИЕ ИХ ПРЕОБРАЗОАНИЯ В ШЕСТНАдЦАТИРИЧНЫЙ ВИД
    for i in range(len(arr_div_num)):
        if arr_div_num[i] >= 10:
             if arr_div_num[i] == 10:
                 hex_num += hex_nums[10]
             elif arr_div_num[i] == 11:
                 hex_num += hex_nums[11]
             elif arr_div_num[i] == 12:
                 hex_num += hex_nums[12]
             elif arr_div_num[i] == 13:
                 hex_num += hex_nums[13]
             elif arr_div_num[i] == 14:
                 hex_num += hex_nums[14]
             elif arr_div_num[i] == 15:
                 hex_num += hex_nums[15]
        else:
            hex_num += str(arr_div_num[i])

    return hex_num



def main():
    user_num_str = input("Введите целое число: ")
    user_num = 0

    hex_nums = "0123456789ABCDEF"
    total_num = ""

# ОТРАБОТКА УСЛОВИЯ НА ВВОДА 0
    if user_num_str == "0":
        total_num = 0
    else:
        # ОБРАБОТКА УСЛОВИЯ НА ВВОД ОТРИЦАТЕЛЬНОГО ЗНАЧЕНИЯ
        negative_char = user_num_str.find("-") # ПОИСК МИНУСА С ПОМОЩЬЮ МЕТОДА find(КОТОРЫЙ ВОЗВРАЩАЕТ ИНДЕКС, ЕСЛИ ДАННЫЙ СИМВОЛ НАХОДИТСЯ В СТРОКЕ
                                               # И ВОЗВРАЩАЕТ -1, ЕСЛИ ДАННОГО СИМВОЛА НЕТ В СТРОКЕ )

        if negative_char >= 0:
            total_num = "-"
            user_num = abs(int(user_num_str))
            print("Отрицательное число")
        else:
            total_num = ""
            user_num = int(user_num_str)


        val_func_hex = hex_func(user_num, hex_nums)

        total_num += val_func_hex


# ВЫВОД НА ЭКРАН ИТОГОВОГО ЗНЕАЧЕНИЯ
    print("HEX - ", total_num)

if __name__ == '__main__':
    main()

