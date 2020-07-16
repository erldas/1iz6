def palindrom():
    a = str(input())
    b =''.join(reversed(a))
    # print(b)
    if a == b:
        print('True')
    
    else:
        print('False')

palindrom()


# Напишите функцию, которая будет определять палиндром ли введенная
# строка. Если да, то напечатать “True”, если нет -“False”.