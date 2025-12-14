import numpy as np

def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    n = len(b)
    x = np.zeros(n)

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            sigma1 = sum(A[i][j] * x[j] for j in range(i))
            sigma2 = sum(A[i][j] * x_old[j] for j in range(i+1, n))
            x[i] = (b[i] - sigma1 - sigma2) / A[i][i]

        error = np.linalg.norm(x - x_old, ord=np.inf)
        print(f"Iterasi {k+1}: x = {x}, error = {error}")

        if error < tol:
            break

    return x

A = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]], float)

b = np.array([27, -61.5, -21.5], float)

solusi = gauss_seidel(A, b)
print("\nSolusi akhir:", solusi)
