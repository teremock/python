def naiti_obiom(vysota, dlinna, shirina):
    obiom = naiti_ploshad_osnovania(dlinna, shirina) * vysota
    print('Обьём паралелепипеда',obiom,'куб.см.')
    return obiom

def int_input(text):
    vvod = ''
    while not vvod.isdigit():
        print(text + ':')
        vvod = input()
    return int(vvod)

def naiti_ploshad_osnovania(dlinna, shirina):
    return shirina * dlinna

def poluchit_razmer():
    razmery = []
    razmery.append(int_input('Ввведите высоту паралелепипеда'))
    razmery.append(int_input('Ввведите длину паралелепипеда'))
    razmery.append(int_input('Ввведите ширину паралелепипеда'))

    return razmery
print('Вычисляем обьём паралелепипеда')
new_obiom = poluchit_razmer()
naiti_obiom(new_obiom[0], new_obiom[1], new_obiom[2])