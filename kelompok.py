'''

Semoga terbantu dengan adanya tool ini <3
Day 3 Kuliah njier

- Created by BAY406 -

'''

import random
import math

try:
    jumlah_kelompok = int(input("Masukkan Jumlah Kelompok Yang Ingin Dibuat: "))
    file_path = input("Masukkan Letak File Data Kelompok (contoh: data.txt): ")

    with open(file_path, 'r') as file:
        semua_anggota = [line.strip() for line in file if line.strip()]

    random.shuffle(semua_anggota)

    total_anggota = len(semua_anggota)
    anggota_per_kelompok = math.ceil(total_anggota / jumlah_kelompok)

    print("\n--- Hasil Pembagian Kelompok ---")

    for i in range(jumlah_kelompok):
        awal = i * anggota_per_kelompok
        akhir = awal + anggota_per_kelompok
        kelompok_saat_ini = semua_anggota[awal:akhir]
        
        if kelompok_saat_ini:
            print(f"\n--- Kelompok {i + 1} ---")
            for anggota in kelompok_saat_ini:
                print(f"- {anggota}")

except FileNotFoundError:
    print(f"Error: File tidak ditemukan di lokasi '{file_path}'")
except ValueError:
    print("Error: Harap masukkan angka yang valid untuk jumlah kelompok.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
