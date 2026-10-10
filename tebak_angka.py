import random

rahasia = random.randint(1, 10)
benar = False
jumlah=0
while benar == False:
    tebakan = int(input("Tebak angka 1 sampai 10: "))
    if tebakan == rahasia:
        print("Benar")
        benar=True
    elif tebakan <rahasia:
        print("Terlalu kecil")
    else:
        print("Terlalu Besar")
    jumlah= jumlah + 1
    print("kamu butuh", jumlah, "kali tebakan")