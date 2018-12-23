from scipy.optimize import minimize_scalar
import math as m
from multiprocessing.dummy import Pool as TPool

out = open("Results 1.2 Num.md", "w")


def calculate(x1_old, x2_old, eps, method, details=False):
    i = 0
    calls = 0

    def func(x1, x2):
        return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2

    def func_for_minimize(x):
        # Вместо x1 и x2 подставлены выражения для x1_new и x2_new,
        # чтобы использовать функцию в минимизации скаляра
        return 100 * ((x2_old - x * g2) - (x1_old - x * g1) ** 2) ** 2 + (1 - (x1_old - x * g1)) ** 2

    if details:
        out = open("Details.md", "w")
        out.write(f"## Начальная точка: **{(x1_old, x2_old)}**, точность: **{eps}**\n\n")
        out.write("| # | x1 | x2 | g1 | g2 | lambda | f |\n")
        out.write("| --- | --- | --- | --- | --- | --- | --- |\n")

    while True:
        if method == "analytic":
            g1 = -400 * x1_old * (x2_old - x1_old ** 2) - 2 * (1 - x1_old)
            g2 = 200 * (x2_old - x1_old ** 2)
        else:
            g1 = (func(x1_old + eps, x2_old) - func(x1_old, x2_old)) / eps
            g2 = (func(x1_old, x2_old + eps) - func(x1_old, x2_old)) / eps
            calls += 2

        lamb = minimize_scalar(func_for_minimize, method="golden")
        calls += lamb.nit
        x1_new = x1_old - lamb.x * g1
        x2_new = x2_old - lamb.x * g2
        i = i + 1
        if details:
            out.write(
                f"| **{i}** | {x1_new:0.9f} | {x2_new:0.9f} | {g1:0.9f} | {g2:0.9f} | {lamb.x:0.9f} | {func(x1_new, x2_new):0.9f} |\n")
        if abs(x2_old - x2_new) < eps and abs(x1_old - x1_new) < eps:
            break
        # if m.sqrt(g1 ** 2 + g2 ** 2) < eps:
        #     break
        x1_old = x1_new
        x2_old = x2_new

    f = func(x1_old, x2_old)
    if details:
        out.write(f"\nПолученное приближение: ({x1_old:0.9f}, {x2_old:0.9f})  \n")
        out.write(f"Значение функции: {f:0.9f}  \n")
        out.write(f"Количество итераций: {i}\n\n")
        out.close()

    return i, calls, x1_old, x2_old, f


def calc_and_print(params):
    res = calculate(params[0], params[1], params[2], "numeric")
    print(res)
    out.write(
        f"| {params[0]} | {params[1]} | {res[0]} | {res[1]} | {res[2]:0.9f} | {res[3]:0.9f} | {res[4]:0.9f} |\n")


out.write("# Подробные данные к ЛР 1.2\n")
out.write("## Аналитическое вычисление градиента\n")
for eps in [1e-3, 1e-5, 1e-7]:
    pool = TPool(8)
    data = []
    out.write(f"### Точность: {eps}\n")
    out.write("| x1_0 | x2_0 | iterations | calls | x1_res | x2_res | f(x_res) |\n")
    out.write("| --- | --- | --- | --- | --- | --- | --- |\n")
    for i in range(-4, 5):
        for j in range(-4, 5):
            data.append((i, j, eps))
    pool.map(calc_and_print, data)
    pool.close()
    pool.join()
    out.write("\n")
