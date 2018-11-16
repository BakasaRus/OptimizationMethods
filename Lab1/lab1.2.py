from scipy.optimize import minimize_scalar
import math as m

eps = 1e-3
i = 0
x1_old = -2
x2_old = 2
out = open("Results 1.2.md", "w")


def func(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def func_for_minimize(x):
    # Вместо x1 и x2 подставлены выражения для x1_new и x2_new,
    # чтобы использовать функцию в минимизации скаляра
    return 100 * ((x2_old - x * g2) - (x1_old - x * g1) ** 2) ** 2 + (1 - (x1_old - x * g1)) ** 2


out.write("# Подробные данные к ЛР 1.2\n\n")
out.write("## Начальная точка: **{}**, точность: **{}**\n\n".format((x1_old, x2_old), eps))
out.write("| # | x1 | x2 | f |\n")
out.write("| --- | --- | --- | --- |\n")
while True:
    g1 = -400 * x1_old * (x2_old - x1_old ** 2) - 2 * (1 - x1_old)
    g2 = 200 * (x2_old - x1_old ** 2)
    l = minimize_scalar(func_for_minimize)
    x1_new = x1_old - l.x * g1
    x2_new = x2_old - l.x * g2
    if m.sqrt(g1 ** 2 + g2 ** 2) < eps:
        break
    # if abs(func(x1_new, x2_new) - func(x1_old, x2_old)) < eps:
    #     break
    x1_old = x1_new
    x2_old = x2_new
    i = i + 1
    if i % 100 == 0:
        out.write("| **{}** | {:0.9f} | {:0.9f} | {:0.9f} |\n".format(i, x1_old, x2_old, func(x1_old, x2_old)))

out.write("\nПолученное приближение: ({:0.9f}, {:0.9f})  \n".format(x1_old, x2_old))
out.write("Значение функции: {:0.9f}  \n".format(func(x1_old, x2_old)))
out.write("Количество итераций: {}\n\n".format(i))
print((x1_old, x2_old, i))
