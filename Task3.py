# TASK3

def transfer_to_roman(user_num):

    arr_roman = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                 (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                 (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
                 (1, "I")]

    roman = ""

    while user_num > 0:
        # ПЕРЕБИРАЕМ ВСЕ ПАРЫ ИЗ СЛОВАРЯ
        for i, j in arr_roman:
            # ВЫПОЛНЯЕМ ДО ТЕХ ПОР ПОКА ЧИСЛО БОЛЬШЕ ИЛИ РАВНО ЧИСЛУ ИЗ СЛОВАРЯ
            while user_num >= i:
                roman += j  # ДОБАВЛЯЕМ СООТВЕТСТВУЮЩУЮ БУКВУ В РИМСКОЕ ЧИСЛО

                # ВЫЧИТАЕМ СЛОВАРНОЕ ЧИСЛО ИЗ НАШЕГО ЧИСЛА
                user_num -= i

    return roman



def main():
    user_num = int(input("Введите целое число: "))

    roman_num = transfer_to_roman(user_num)

    print("РИМСКОЕ ЧИСЛО: ", roman_num)

if __name__ == '__main__':
    main()