# Dictionary Example in Python

# Membuat dictionary
siswa = {
    "nama": "Imam",
    "umur": 19,
    "kelas": "TI-1"
}
print("Dictionary awal:", siswa)

# Mengakses nilai
print("Nama siswa:", siswa["nama"])

# Menambah key-value baru
siswa["kota"] = "Tangerang"
print("Setelah menambah kota:", siswa)

# Mengubah nilai
siswa["umur"] = 19
print("Setelah update umur:", siswa)

# Menghapus key-value
siswa.pop("kelas")
print("Setelah menghapus kelas:", siswa)

# Looping dictionary
print("\nLooping dictionary:")
for key, value in siswa.items():
    print(key, ":", value)
