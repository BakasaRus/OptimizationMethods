def find_path(g, start, end):
    g_size = len(g)
    l = [1000] * g_size
    path = [[]] * g_size
    l[start] = 0
    path[start] = [start]
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            l[j] = min(l[j], l[i] + g[i][j])
            if l[j] == l[i] + g[i][j]:
                path[j] = path[i] + [j]
    return l, path


input = open("graph.txt", "r")
# В первой строчке у нас количество вершин и номера начальной и конечной вершин
size, start, end = [int(s) for s in input.readline().split(" ")]
g = []
for i in range(size):
    g.append([1000] * size)

# В остальных строчках у нас рёбра в виде "start end weight"
for line in input.readlines():
    a, b, weight = [int(s) for s in line.split(" ")]
    g[a - 1][b - 1] = weight

input.close()

length, path = (find_path(g, start - 1, end - 1))
str_path = " -> ".join(map(lambda x: str(x + 1), path[end - 1]))
print(f"Кратчайший путь: {str_path}")
print(f"Длина кратчайшего пути от {start} до {end} равен {length[end - 1]}")
