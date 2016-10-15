import teremok_util
import random
import time

def greeting():
    print('Давай поиграем в игру "Запомни Числа"! Я буду показывать 5 чисел на несколько секунд, тебе надо их запомнить и ввести.')

def get_input(max):
    numbers = []
    for step1 in range(0,max):
       numbers.append(teremok_util.int_input('Введите число ' + str(step1 + 1) + ' из ' + str(max)))
    return numbers

def generate_numbers(max_count, max_number):
    numbers = []
    print('Запомни эти числа:')
    for count in range(0, max_count):
        random_number = random.randint(1, max_number)
        while random_number in numbers:
          random_number = random.randint(1, max_number)
        numbers.append(random_number)
    print(numbers)
    time.sleep(10)
    print('\n' * 50)
    return numbers

def matches(vopros, otvet):
    prav_otvety_seichas = 0
    for n in vopros:
        if n in otvet:
            prav_otvety_seichas = prav_otvety_seichas + 1
    return prav_otvety_seichas

prav_otvety = 0
vsego_zagadano = 0
otvet = []
vopros = []
number_of_digits = 5
level = 1
max_level = 10

greeting()

while level <= 10:
    vopros = generate_numbers(number_of_digits, level * 10)
    otvet = get_input(number_of_digits)
    prav_otvety_seichas = matches(vopros, otvet)
    print('Вы угадали', prav_otvety_seichas , 'чисел')
    prav_otvety += prav_otvety_seichas
    vsego_zagadano += number_of_digits
    percent = teremok_util.percent(prav_otvety, vsego_zagadano)
    print('Это', percent , '% попаданий')
    if percent > 50:
        level = level + 1
    print('Уровень', level)

print('Вы МЕГА-МОЗГ!!!!!')