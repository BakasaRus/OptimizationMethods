from scipy.optimize import minimize_scalar
import math as m

eps = 1e-3
i = 0
x1_old = -2
x2_old = 2
out = open("Results 1.2 Numerically.md", "w")


def func(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def func_for_minimize(x):
    # Вместо x1 и x2 подставлены выражения для x1_new и x2_new,
    # чтобы использовать функцию в минимизации скаляра
    return 100 * ((x2_old - x * g2) - (x1_old - x * g1) ** 2) ** 2 + (1 - (x1_old - x * g1)) ** 2


out.write("# Подробные данные к ЛР 1.2\n\n")
out.write(f"## Начальная точка: **{(x1_old, x2_old)}**, точность: **{eps}**\n\n")
out.write("| # | x1 | x2 | g1 | g2 | lambda | f |\n")
out.write("| --- | --- | --- | --- | --- | --- | --- |\n")
while True:
    # g1 = -400 * x1_old * (x2_old - x1_old ** 2) - 2 * (1 - x1_old)
    # g2 = 200 * (x2_old - x1_old ** 2)

    g1 = (func(x1_old + eps, x2_old) - func(x1_old, x2_old)) / eps
    g2 = (func(x1_old, x2_old + eps) - func(x1_old, x2_old)) / eps

    lamb = minimize_scalar(func_for_minimize).x
    x1_new = x1_old - lamb * g1
    x2_new = x2_old - lamb * g2
    i = i + 1
    # if i % 100 == 0:
    out.write(
        f"| **{i}** | {x1_new:0.9f} | {x2_new:0.9f} | {g1:0.9f} | {g2:0.9f} | {lamb:0.9f} | {func(x1_new, x2_new):0.9f} |\n")
    if m.sqrt(g1 ** 2 + g2 ** 2) < eps:
        break
    # if abs(func(x1_new, x2_new) - func(x1_old, x2_old)) < eps:
    #     break
    # if abs(x2_old - x2_new) < eps and abs(x1_old - x1_new) < eps:
    #     break
    x1_old = x1_new
    x2_old = x2_new

out.write(f"\nПолученное приближение: ({x1_old:0.9f}, {x2_old:0.9f})  \n")
out.write(f"Значение функции: {func(x1_old, x2_old):0.9f}  \n")
out.write(f"Количество итераций: {i}\n\n")
