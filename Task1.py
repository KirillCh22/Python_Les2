import math

def GCD(first_num, second_num):

    while first_num != 0 and second_num != 0:

        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num

    return first_num + second_num



def main():
    num1 = int(input("Введите 1-ое число: "))
    num2 = int(input("Введите 2-ое число: "))

    num_GCD = GCD(first_num=num1, second_num=num2)
    num_gcd2 = math.gcd(num1, num2)

    print("НОД чисел = ", num_GCD, num_gcd2)



if __name__ == '__main__':
    main()

