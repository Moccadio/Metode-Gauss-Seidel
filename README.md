# Gauss-Seidel Method (Python)

Program numerik sederhana untuk **menyelesaikan sistem persamaan linear** menggunakan **Metode Gauss-Seidel**, dibangun menggunakan **Python** dan **NumPy**.

---

## Deskripsi Umum Proyek

**Gauss-Seidel Method Program** digunakan untuk menghitung solusi sistem persamaan linear secara **iteratif**.  
Program akan memperbarui nilai setiap variabel dengan memanfaatkan nilai terbaru pada iterasi yang sama hingga solusi **konvergen** atau mencapai batas iterasi maksimum.

Selain itu, program menampilkan **hasil setiap iterasi** (nilai x) beserta **nilai error** menggunakan norma tak hingga (∞-norm).

---

## Tujuan

1. Mengimplementasikan metode iteratif **Gauss-Seidel** menggunakan Python.  
2. Menyelesaikan sistem persamaan linear berbasis matriks `A` dan vektor `b`.  
3. Menampilkan proses iterasi dan nilai error untuk memantau konvergensi.  
4. Menampilkan solusi akhir ketika memenuhi toleransi error.

---

## Fitur Utama

| Fitur | Deskripsi |
|------:|-----------|
| Iterasi Gauss-Seidel | Menghitung solusi secara bertahap (iteratif) |
| Error Checking | Menggunakan norma tak hingga (∞-norm) |
| Output Iterasi | Menampilkan nilai x dan error di setiap iterasi |
| Solusi Akhir | Menampilkan solusi akhir setelah konvergen |

---

## Struktur Data / Parameter

| Parameter | Tipe | Keterangan |
|----------|------|------------|
| `A` | array (n×n) | Matriks koefisien sistem persamaan |
| `b` | array (n) | Vektor konstanta |
| `tol` | float | Toleransi error (default `1e-6`) |
| `max_iter` | int | Batas iterasi maksimum (default `100`) |

---

## Contoh Sistem Persamaan

Sistem persamaan yang diselesaikan (sesuai kode):
10x + 2y - z = 27
-3x - 6y + 2z = -61.5
x + y + 5z = -21.5


Representasi pada program:
```python
A = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]], float)

b = np.array([27, -61.5, -21.5], float)
```
## Contoh Sistem Persamaan
Program menampilkan output tiap iterasi:
Iterasi 1: x = [...], error = ...
Iterasi 2: x = [...], error = ...
...
Solusi akhir: [...]
