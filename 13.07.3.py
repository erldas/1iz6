a = [1, -4, 44, 8, -10]
def bagaj(x):
    if x < 0:
        return True
    else:
        return False

b = filter(bagaj, a)
b = list(b)


def bag(y):
    if y > 0:
        return True
    else:
        return False
c = filter(bag, a)
c = list(c)

print(c)

print(b)






# Напишите программу, где исходный список содержит положительные и
# отрицательные числа. Требуется положительные поместить в один
# список, а отрицательные - в другой(Используйте встроенные функции,
# чтобы решить эту задачу)