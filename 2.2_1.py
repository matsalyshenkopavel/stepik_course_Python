"""В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит,
когда с момента исходной даты date пройдет число дней, равное days."""


import datetime

full_date = list(map(int, input().split()))
date = datetime.date(full_date[0], full_date[1], full_date[2])
answer = date + datetime.timedelta(days=int(input()))
print(answer.year, answer.month, answer.day)