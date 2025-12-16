# Gauss-Seidel Method (Python)

A simple numerical program for **solving systems of linear equations** using the **Gauss-Seidel Method**, built with **Python** and **NumPy**.

---

## Project Overview

The **Gauss-Seidel Method Program** is used to compute the solution of a system of linear equations **iteratively**.  
The program updates each variable using the most recent values within the same iteration until the solution **converges** or reaches the maximum number of iterations.

In addition, the program displays the **iteration results** (solution vector `x`) along with the **error value** calculated using the infinity norm (∞-norm).

---

## Objectives

1. Implement the **Gauss-Seidel iterative method** using Python.  
2. Solve systems of linear equations based on matrix `A` and vector `b`.  
3. Display the iteration process and error values to monitor convergence.  
4. Output the final solution once the error tolerance is satisfied.

---

## Key Features

| Feature | Description |
|-------:|-------------|
| Gauss-Seidel Iteration | Computes solutions iteratively |
| Error Checking | Uses infinity norm (∞-norm) |
| Iteration Output | Displays solution vector and error at each iteration |
| Final Solution | Outputs the converged solution |

---

## Data Structure / Parameters

| Parameter | Type | Description |
|----------|------|-------------|
| `A` | array (n×n) | Coefficient matrix of the linear system |
| `b` | array (n) | Constant vector |
| `tol` | float | Error tolerance (default `1e-6`) |
| `max_iter` | int | Maximum number of iterations (default `100`) |

---

## Example System of Equations

The system of equations solved by the program:


Sistem persamaan yang diselesaikan (sesuai kode):
10x + 2y - z = 27
-3x - 6y + 2z = -61.5
x + y + 5z = -21.5

## Code Representation

```python
A = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]], float)

b = np.array([27, -61.5, -21.5], float)

```
## Output
```python
Iteration 1: x = [...], error = ...
Iteration 2: x = [...], error = ...
...
Final solution: [...]
```
