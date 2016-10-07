def naiti_obiom(vysota, dlinna, shirina):
    obiom = naiti_ploshad_osnovania(dlinna, shirina) * vysota
    return obiom

def naiti_ploshad_osnovania(dlinna, shirina):
    return shirina * dlinna

def poluchit_razmer():
    razmery = []
    razmery.append(int(input('Ввведите высоту парралелепипеда:')))
    razmery.append(int(input('Ввведите длину парралелепипеда:')))
    razmery.append(int(input('Ввведите ширину парралелепипеда:')))

    return razmery

new_obiom = poluchit_razmer()
print(naiti_obiom(new_obiom[0], new_obiom[1], new_obiom[2]))