import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    print("Saya telah memilih sebuah angka antara 1 sampai 100.")
    print("Coba tebak angkanya!")

    while True:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Anda benar menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat saja.")

if __name__ == "__main__":
    tebak_angka()
