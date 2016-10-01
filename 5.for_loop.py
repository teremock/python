def loop_print(marks, number_func):
    number_func = '10'
    print(number_func)
    digit = 10
    for digit in marks:
        print('оценка: ', digit)
        if number == digit:
            print('- это моя оценка')

number = int(input('Введите свою оценку:'))
marks =[1,2,3,4,5]
loop_print(marks, number)
print(number)