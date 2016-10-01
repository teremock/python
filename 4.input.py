def int_input(mult1, mult2):
    if mult1.isdigit() and  mult2.isdigit():
        number1 = int(mult1)
        number2 = int(mult2)
        if number2 > 0:
            return number1 * number2
        else:
            return number1
    else:
        print('Вы ввели некорректные значения!')
        quit()
print ('Введите множители:')
mult =  int_input(input(), input())
print ('Введите число:')
result = int_input(input(), mult)
print ('Результат умножения:', result)

