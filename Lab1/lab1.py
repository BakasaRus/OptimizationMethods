import math as m
from Lab1.odsearch import dichotomy, golden, fibonacci

out = open("Lab1/Results.md", "w")
func = lambda x: m.sin(x)
a0 = -m.pi / 2
b0 = m.pi / 2

out.write("# Подробные данные к ЛР 1.1\n")
print("Метод дихотомии")
out.write("## Метод дихотомии\n")
print(dichotomy(func, a0, b0, 1e-3, out))
print(dichotomy(func, a0, b0, 1e-5, out))
print(dichotomy(func, a0, b0, 1e-7, out))

print("Метод золотого сечения")
out.write("## Метод золотого сечения\n")
print(golden(func, a0, b0, 1e-3, out))
print(golden(func, a0, b0, 1e-5, out))
print(golden(func, a0, b0, 1e-7, out))

print("Метод Фибоначчи")
out.write("## Метод Фибоначчи\n")
print(fibonacci(func, a0, b0, 1e-3, out))
print(fibonacci(func, a0, b0, 1e-5, out))
print(fibonacci(func, a0, b0, 1e-7, out))
