# Set Example in Python

# Membuat set
angka = {1, 2, 3, 4}
print("Set awal:", angka)

# Menambah elemen
angka.add(5)
print("Set setelah add:", angka)

# Menghapus elemen
angka.discard(2)
print("Set setelah discard 2:", angka)

# Set tidak menyimpan elemen duplikat
angka.add(3)
print("Set setelah menambah 3 lagi (tidak berubah):", angka)

# Operasi himpunan
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)
