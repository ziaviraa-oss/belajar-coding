#fungsi untuk penjumlahan
def tambah(a, b):
        return a + b
# fungsi untuk pengurangan
def kurang (a, b):
        return a-b

print ("Pilih Operasi:")
print ("1. Tambah (+)")
print ("2. Kurang (-)")

pilihan = input("Masukan pilihan (1/2): ")

angka1 = float(input("Masukan angka pertama:"))
angka2 = float(input("Masukan angka kedua:"))

if pilihan =='1':
    print("Hasilnya:", tambah(angka1, angka2))
elif pilihan =='2':
    print("Hasilnya:", kurang(angka1, angka2))
else:
    print("Pilihan tidak valid!")

    def tambah(a, b):
        return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error! Tidak bisa membagi dengan angka nol."
    return a / b

# Perulangan while agar kalkulator tidak langsung tertutup setelah selesai
while True:
    print("\n--- KALKULATOR SEDERHANA ---")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    # Jika memilih keluar
    if pilihan == '5':
        print("Terima kasih sudah menggunakan kalkulator!")
        break

    # Cek apakah pilihan valid
    if pilihan in ('1', '2', '3', '4'):
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Oops! Harap masukkan angka yang benar ya.")
            continue

        if pilihan == '1':
            print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
        elif pilihan == '2':
            print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
        elif pilihan == '4':
            print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
    else:
        print("Pilihan tidak valid, silakan pilih angka 1 sampai 5.")