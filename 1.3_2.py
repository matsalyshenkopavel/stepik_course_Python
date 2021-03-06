"""Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).

Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Ваша программа должна вывести единственное число: C(n, k).
"""


n, k = map(int, input().split())
def rec(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return rec(n - 1, k) + rec(n - 1, k - 1)

print(rec(n, k))