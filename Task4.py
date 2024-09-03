from fractions import Fraction


def sum_multi_fraction(first_fraction, second_fraction, symbol_operation):

    # ПРЕОБРАЗОВАНИЕ ДРОБИ В ЧИСЛИТЕЛЬ И ЗНАМЕНАТЕЛЬ С ПОМОЩЬЮ МТЕОДА map()
    # numerator - числитель
    # denominator - знаменатель
    numerator_frac1, denominator_frac1 = map(int, first_fraction.split("/"))
    numerator_frac2, denominator_frac2 = map(int, second_fraction.split("/"))


    # СОЗДАЕМ ОБЪЕКТ КЛАССА Fraction, КОТОРЫЙ ПРЕОБРАЗУЕТ ИЗ ЧИСЛИТЕЛЯ И ЗНАМЕНАТЕЛЯ ДРОБЬ
    fraction_val1 = Fraction(numerator_frac1, denominator_frac1)
    fraction_val2 = Fraction(numerator_frac2, denominator_frac2)

    total_val = 0

    # В ЗАВИСИМОСТИ ОТ ТОГО, КАКУЮ ОПЕРАЦИЮ ВВЕЛ ПОЛЬЗОВАТЕЛЬ, ПРОГРАММУ СЧИТАЕТ ДРОБИ
    if symbol_operation == "+":
        total_val = fraction_val1 + fraction_val2
    elif symbol_operation == "*":
        total_val = fraction_val1 * fraction_val2
    elif symbol_operation == "/":
        total_val = fraction_val1 / fraction_val2
    else:
        print("\nВы ввели не существующую операцию!")


    return total_val




def main():
    first_fraction = input("Введите 1-ю дробь типа (a/b): ")
    second_fraction = input("Введите 2-ю дробь типа (a/b): ")
    symbol_operation = input("Введите символ, что вы хотите сделать с дробями: ")

    value = sum_multi_fraction(first_fraction, second_fraction, symbol_operation)

    print("\nОперация {0} с дробями {1} {2} равна: {3}".format(symbol_operation, first_fraction, second_fraction, value))

if __name__ == '__main__':
    main()

