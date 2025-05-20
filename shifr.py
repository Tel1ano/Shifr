up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
low = list('abcdefghijklmnopqrstuvwxyz')
symvol = list('0123456789+-*/_=.,?!;: ')
l_l = len(up)

def into(word):
    result = ''
    def check_len(el, arr):
         nonlocal result
         if (l_l - 1) - arr.index(el) < 4:
            result += arr[(arr.index(el) + 3 - l_l)] 
         else:
            result += arr[(arr.index(el) + 3)]

    for i in list(word):

        for u in up:
            if i==u:
                check_len(u, up)              
        
        for l in low: 
            if i==l:
                check_len(l, low)

        if i in symvol:
                result += i


    return result

def out(word):
    result = ''
    marker = False

    def res(el, arr):
        nonlocal result
        result += arr[(arr.index(el) -3)]

    for i in list(word):

        for u in up: 
            if i==u:
                res(u, up)

        for l in low:
            if i==l:
                res(l, low)

        if i in symvol:
            result += i
    return result

print("""
Виберіть режим:

Зашифрувати   (1)
Розшифрувати  (2)

Твій вибір:
""", end='')

choice = str(input())

if choice == '1':
    word = str(input('Введіть текст який хочете зашифрувати\n'))
    print('Результат:  ', into(word))

elif choice == '2':
    word = str(input('Введіть текст який хочете зашифрувати\n'))
    print('Результат:  ', out(word))

else:
    print('\033[31mError number!\033[0m')

