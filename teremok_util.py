def int_input(text):
    vvod = ''
    while not vvod.isdigit():
        print(text + ':')
        vvod = input()
    return int(vvod)

def percent(num, total):
    return round((num / total) * 100, 2)