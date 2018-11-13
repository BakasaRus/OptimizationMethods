import math as m
import os

PHI = 1.6180339887


def dichotomy(f, a, b, eps, out=open(os.devnull, 'w')):
    counter = 0
    delta = eps * 0.48  # delta < eps / 2
    length = b - a
    out.write("### Интервал: **[{:0.9f}; {:0.9f}]**, точность: **{}**\n".format(a, b, eps))
    out.write("| # | Левая граница | Правая граница | Отношение длин | x1 | f(x1) | x2 | f(x2) |\n")
    out.write("| --- | --- | --- | --- | --- | --- | --- | --- |\n")
    while length >= eps:
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        f1 = f(x1)
        f2 = f(x2)
        if f1 < f2:
            b = x2
        else:
            a = x1
        counter += 1
        out.write("| **{}** | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} |\n"
                  .format(counter, a, b, (b - a) / length, x1, f1, x2, f2))
        length = b - a
    res = (a + b) / 2
    calls = counter * 2
    out.write("\nРезультат: **{:0.9f}**  \n".format(res))
    out.write("Количество вычислений функции: **{}**\n\n". format(calls))
    return res, calls


def golden(f, a, b, eps, out=open(os.devnull, 'w')):
    counter = 0
    x1 = b - (b - a) / PHI
    x2 = a + (b - a) / PHI
    f1 = f(x1)
    f2 = f(x2)
    length = b - a
    out.write("### Интервал: **[{:0.9f}; {:0.9f}]**, точность: **{}**\n".format(a, b, eps))
    out.write("| # | Левая граница | Правая граница | Отношение длин | x1 | f(x1) | x2 | f(x2) |\n")
    out.write("| --- | --- | --- | --- | --- | --- | --- | --- |\n")
    while length >= eps:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - (x1 - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (b - x2)
            f1 = f(x1)
        counter += 1
        out.write("| **{}** | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} |\n"
                  .format(counter, a, b, (b - a) / length, x1, f1, x2, f2))
        length = b - a
    res = (a + b) / 2
    calls = counter + 2
    out.write("\nРезультат: **{:0.9f}**  \n".format(res))
    out.write("Количество вычислений функции: **{}**\n\n". format(calls))
    return res, calls


def fib(n):
    return (PHI**n - (1 - PHI)**n) / m.sqrt(5)


def fibonacci(f, a, b, eps, out=open(os.devnull, 'w')):
    counter = 0
    n = m.ceil(m.log((b - a) * m.sqrt(5) / eps) / m.log(PHI))
    x1 = a + (b - a) * fib(n - 2) / fib(n)
    x2 = a + (b - a) * fib(n - 1) / fib(n)
    f1 = f(x1)
    f2 = f(x2)
    length = b - a
    out.write("### Интервал: **[{:0.9f}; {:0.9f}]**, точность: **{}**\n".format(a, b, eps))
    out.write("| # | Левая граница | Правая граница | Отношение длин | x1 | f(x1) | x2 | f(x2) |\n")
    out.write("| --- | --- | --- | --- | --- | --- | --- | --- |\n")
    while n > 1:
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            f1 = f2
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            f2 = f1
            f1 = f(x1)
        counter += 1
        out.write("| **{}** | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} | {:0.9f} |\n"
                  .format(counter, a, b, (b - a) / length, x1, f1, x2, f2))
        n -= 1
        length = b - a
    res = (a + b) / 2
    calls = counter + 2
    out.write("\nРезультат: **{:0.9f}**  \n".format(res))
    out.write("Количество вычислений функции: **{}**\n\n". format(calls))
    return res, calls
