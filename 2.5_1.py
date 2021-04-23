"""Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y,
которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе."""

def mod_checker(x, mod=0):
    def lambd(y):
        return y % x == mod
    return lambd