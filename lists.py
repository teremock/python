def find_in_list(list, name):
    return name in list

def find_in_list_long(list, name):
   for n in list:
       if name == n:
           return True
   return False

def half_word(word):
    return word[:int(len(word) / 2)]

def naoborot(word):
    return word[::-1]

def main(list):
    vvod = ''
    while not find_in_list_long(list, vvod):
        print('Здравствуйте, введите имя:')
        vvod = input()

    print(vvod * 2)
    print(half_word(vvod))
    print(naoborot(vvod))

main(['misha','petya','vanya','irina'])

