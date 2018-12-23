import numpy as np
np.set_printoptions(precision=3)


def simplex_max(A, b, c, z=0):
    A = np.hstack((A, np.eye(A.shape[0])))
    c = np.append(c, [0] * A.shape[0])
    c = c * (-1)

    def find_min_row(a, b):
        i = 0
        while a[i] <= 0:
            i += 1
        m = b[i] / a[i]
        argm = i
        for i in range(i + 1, a.size):
            if (a[i] > 0) and (b[i] / a[i] < m):
                m = b[i] / a[i]
                argm = i
        return argm

    i = 1

    while (c < 0).sum():
        s = c.argmin()
        if (A[:, s] > 0).sum() == 0:
            print("function has no limit")
            break
        r = find_min_row(A[:, s], b)
        z -= b[r] / A[r, s] * c[s]
        c = c - A[r, :] / A[r, s] * c[s]

        b_r = b[r]
        A_rj = A[r, :]
        b = b - b[r] / A[r, s] * A[:, s]
        A = A - np.outer(A[:, s], A[r, :] / A[r, s])
        b[r] = b_r / A_rj[s]
        A[r, :] = A_rj / A_rj[s]

        print("Iteration:", i)
        print('r:', r, ";", 's:', s)
        print(A)
        print('b', b)
        print("c", c)
        print('z', z)
        print()
        i += 1

    return z


A = np.array([[1, 2, -1, 2, 4],
              [0, -1, 2, 1, 3],
              [0, -1, 2, 1, 3]])
b = np.array([1, 3, 4])
c = np.array([1, -3, 2, 1, 4])
z = 0

simplex_max(A, b, c)
