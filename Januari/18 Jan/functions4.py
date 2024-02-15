# def func(value):
#     return value, value*2, value*3


# return_value = func(10)
# print(return_value)


# def func(value):
#     return value, value*2, value*3


# a, b, c = func(10)
# print(a)
# print(b)
# print(c)


# def func(value):
#     return value, value*2, value*3, value*4


# t = (1, 3, 7, 5, 8)

# first, *rest, last = t
# print(first)
# print(last)
# print(rest)


def func(value):
    return value, value*2, value*3, value*4


a, *b, c = func(10)
print(a)
print(b)
print(c)