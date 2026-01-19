import os
os.system("cls")

DATA_PELANGGAN = "data_pelanggan_kiloan.txt","data_pelanggan_satuan"

#transisi
def enter():
  input("\n\t\t\tklik --> { Enter } <-- untuk melanjutkan... ")

#untuk membersihkan layar
def clear():
  os.system("cls" if os.name == "nt" else "clear")

# Header Tampilan Program
def header():
  clear()
  print("|","=" * 68,"|")
  print(r" |===  |||||} || |||      ||| |||||||| |||||||| ||||||\  \\    //  ===|")
  print(r" |===  ||     || |||\\  //||| ||    ||    ||    ||   ||}  \\  //   ===|")
  print(r" |===  |||||  || ||  \||/  || ||||||||    ||    |||/\//    \\//    ===|")
  print(r" |===     ||  || ||   ||   || ||    ||    ||    |||  \|\    ||     ===|")
  print(r" |=== {|||||  || ||        || ||    ||    ||    |||   \|\   ||     ===|")
  print("/","_"*68,"\\")
  print("|"+"SYSTEM MANAGEMENT LAUNDRY".center(70)+"|")
  print("|","=" * 68,"|")

# halaman login
def login():
  while True:
    header()
    print("|"+"------------------------{] Halamana Log-in [}-------------------------".center(70)+"|")
    kasir=input("\n\t\t\tUser Nami\t: ").strip()
    pw=input("\t\t\tPassword\t: ")
    clear()
# VALIDASI NAMA KOSONG
    if kasir == "":
      clear()
      header()
      print("\n|" + "-------------------------{] PERINGATAN ❗ [}--------------------------|".center(70))
      print("|" + "_______________________NAMA_TIDAK_BOLEH_KOSONG________________________|")
      enter()
      clear()
      continue   # kembali ke awal loop
# VALIDASI PASSWORD
    elif pw == "sesama":
      header()
      print("\n|"+"-----------------------{] Login berhasil ✅ [}------------------------|".center(70))
      print("|_________________WELCOME_TO_SISTEM_MANAGEMENT_LAUNDRY_________________|\n".center(71))
      enter()
      break
    else:
      header()
      print("\n|"+"-----------------------{] ❌ Login gagal ❌ [}-----------------------|".center(70))
      print("|"+"_________________PASSWORD_SALAH_!!_Silahkan_coba_lagi_________________"+"|")
      enter()
      clear()
      continue

#halaman utama aplikasi kasir laundry
def halaman_utama():
  clear()
  header()
  print("\t\t|=======================================|".upper())
  print("|            halaman utama              |".center(73))
  print("\t\t|=======================================|".upper())
  print("\t\t|\t1. daftar menu".title()+"\t\t\t|")
  print("\t\t|\t2. buat transaksi".title()+"\t\t|")
  print("\t\t|\t3. daftar member".title()+"\t\t|")
  print("\t\t|\t4. histori pesanan".title()+"\t\t|")
  print("\t\t|\t5. tentang ".title()+"simatry".upper()+"\t\t|")
  print("\t\t|\t6. keluar ".title()+"\t\t\t|")
  print("\t\t|=======================================|\n".upper())

def main():
  login()
  halaman_utama()

main()

#input data pelanggan
def data_pelanggan_kiloan():
  nama = input("Masukkan nama pelanggan : ".title())
  wa = int(input("nomor WA : ".title()))
  pesanan = input("pesanan apa yang diinginkan : ".title())
  match pesanan:
    case "1":
      print("""
pilihan paket laundry kiloan :
1. Cuci + Setrika Reguler   (Rp 7.000/kg)
""")
      harga_kiloan = 7000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      data_pelanggan_kiloan()
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "2":
      print("""pilihan paket laundry kiloan :
2. setrika saja reguler   (Rp 5.000/kg)
""")      
      harga_kiloan = 5000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "3":
      print("""pilihan paket laundry kiloan :
3. cuci saja reguler   (Rp 5.000/kg)
""")
      harga_kiloan = 5000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "4":
      print("""pilihan paket laundry kiloan :
4. Cuci + Setrika Express   (Rp 12.000/kg)
""")
      harga_kiloan = 12000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "5":
      print("""pilihan paket laundry kiloan :
5. setrika saja express   (Rp 8.000/kg)
""")
      harga_kiloan = 8000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "6":
      print("""pilihan paket laundry kiloan :
6. cuci saja express   (Rp 8.000/kg)
""")
      harga_kiloan = 8000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "7":
      print("""pilihan paket laundry kiloan :
7. Cuci + Setrika Express   (Rp 8.000/kg)
""")
      harga_kiloan = 8000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "8":
      print("""pilihan paket laundry kiloan :
8. setrika saja express   (Rp 5.000/kg)
""")
      harga_kiloan = 5000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "9":
      print("""pilihan paket laundry kiloan :
9. cuci saja express   (Rp 5.000/kg)
""")
      harga_kiloan = 5000
      berat = float(input("masukkan berat laundry (kg) : ".title()))
      total = berat * harga_kiloan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()  
    case _:
      print("\nPilihan pesanan tidak valid.")
      return

  with open(DATA_PELANGGAN,"a") as file:
    file.write(f"Nama : {nama}\n")
    file.write(f"WA   : {wa}\n")
    file.write(f"Pesanan : {pesanan}\n")
    file.write("-"*30+"\n")

'''menu laundry dan harga paket'''
def tampilkan_menu():
  print("\nDAFTAR PAKET LAUNDRY")
  print("1. Laundry Kiloan")
  print("2. Laundry Satuan")

def data_pelanggan_satuan():
  nama = input("Masukkan nama pelanggan : ".title())
  wa = int(input("nomor WA : ".title()))
  pesanan_satuan = input("pesanan apa yang diinginkan : ".title())
  match pesanan_satuan:
    case "1":
      print("""pilihan paket laundry satuan :
1. Jaket/Sweater                            | Rp.17500
""")
      harga_satuan = 17500
      total = harga_satuan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "2":
      print("""pilihan paket laundry satuan :
2. Jaket/Sweater Anak                       | Rp.8500
""")
      harga_satuan = 8500
      total = harga_satuan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "3":
      print("""pilihan paket laundry satuan :
3. Jaket Kulit                              | Rp.72000
""")
      harga_satuan = 72000
      total = harga_satuan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "4":
      print("""pilihan paket laundry satuan :
4. Jaket Kulit Anak                         | Rp.35000
""")
      harga_satuan = 35000
      total = harga_satuan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case "5":
        print("""pilihan paket laundry satuan :
5. Jas                                      | Rp.17500
""")
        harga_satuan = 17500
        total = harga_satuan
        print(f"\nTotal yang harus dibayar : Rp {int(total)}")
        print("\nTerima kasih telah menggunakan SIMATRI.")
        kembali = input("Tekan ENTER untuk kembali...")
        main()
    case "6":
        print("""pilihan paket laundry satuan :
6. Jas Anak                                 | Rp.8500
""")
        harga_satuan = 8500
        total = harga_satuan
        print(f"\nTotal yang harus dibayar : Rp {int(total)}")
        print("\nTerima kasih telah menggunakan SIMATRI.")
        kembali = input("Tekan ENTER untuk kembali...")
        main()
    case "7":
        print("""pilihan paket laundry satuan :
7. Jas/Sweater Panjang                      | Rp.17000
""")
        harga_satuan = 17000
        total = harga_satuan
        print(f"\nTotal yang harus dibayar : Rp {int(total)}")
        print("\nTerima kasih telah menggunakan SIMATRI.")
        kembali = input("Tekan ENTER untuk kembali...")
        main()
    case "8":
        print("""pilihan paket laundry satuan :
8. Jas Pria                                 | Rp.17500
""")
        harga_satuan = 17500
        total = harga_satuan
        print(f"\nTotal yang harus dibayar : Rp {int(total)}")
        print("\nTerima kasih telah menggunakan SIMATRI.")
        kembali = input("Tekan ENTER untuk kembali...")
        main()
    case "9":
      print("""pilihan paket laundry satuan :
9. Jubah                                    | Rp.17500
""")
      harga_satuan = 17500
      total = harga_satuan
      print(f"\nTotal yang harus dibayar : Rp {int(total)}")
      print("\nTerima kasih telah menggunakan SIMATRI.")
      kembali = input("Tekan ENTER untuk kembali...")
      main()
    case _:
      print("\nPilihan pesanan tidak valid.")
      return

#menu laundry kiloan
def menu_laundry_kiloan():
  print("""
     ____________________________________________________________
    |     |   Harga Laundry Per Kiloan Terbaru   |               |
    | No. |              Layanan                 |     Harga     |
    |     |                                      |               |
    |------------------------------------------------------------|
    | Reguler ( 2 Hari )                                         |
    |------------------------------------------------------------|
    |  1   |            Cuci + Setrika            |  Rp.7000/Kg  |
    |  2   |             Setrika Saja             |  Rp.5000/Kg  |
    |  3   |              Cuci Saja               |  Rp.5000/Kg  |
    |------------------------------------------------------------|
    | Express 12 Jam                                             |
    |------------------------------------------------------------|
    |  4   |            Cuci + Setrika            |  Rp.12000/Kg |
    |  5   |             Setrika Saja             |  Rp.8000/Kg  |
    |  6   |              Cuci Saja               |  Rp.8000/Kg  |
    |------------------------------------------------------------|
    | Express 24 Jam                                             |
    |------------------------------------------------------------|
    |  7   |            Cuci + Setrika            |  Rp.8000/Kg  |
    |  8   |             Setrika Saja             |  Rp.5000/Kg  |
    |  9   |              Cuci Saja               |  Rp.5000/Kg  |
    |____________________________________________________________|
  """)

#menu laundry satuan
def menu_laundry_satuan():
  print("""       ____________________________________________________________
       |------------------------------------------------------------|
       | No.|              Nama Item Laundry            |   Harga   |
       |------------------------------------------------------------|
       | 1  |  Jaket/Sweater                            | Rp.17500  |
       | 2  |  Jaket/Sweater Anak                       | Rp.8500   |
       | 3  |  Jaket Kulit                              | Rp.72000  | 
       | 4  |  Jaket Kulit Anak                         | Rp.35000  |
       | 5  |  Jas                                      | Rp.17500  |
       | 6  |  Jas Anak                                 | Rp.8500   |
       | 7  |  Jas/Sweater Panjang                      | Rp.17000  |
       | 8  |  Jas Pria                                 | Rp.17500  |
       | 9  |  Jubah                                    | Rp.17000  |
       |____________________________________________________________|
       """)

opsi=int(input("apa yang anda butuhkan : ".title()))
match opsi:
    case 1:
        clear()
        header()
        tampilkan_menu()
        pilih_paketan=int(input("Pilih paket laundry yang diinginkan (1/2) : ".title()))
        if pilih_paketan == 1:
          clear()
          header()
          menu_laundry_kiloan()
        elif pilih_paketan == 2:
          clear()
          header()
          menu_laundry_satuan()
        # menu_laundry_satuan()
        elif pilih_paketan == 3:
          clear()
          header()
          menu_laundry_satuan()
        else:
          print("\nPilihan tidak valid.")
        enter()
    case 2:
        clear()
        header()
        # transaksi()
        enter()
    # case 3:
    #     clear()
    #     header()
    #     print("\n=== DAFTAR MEMBER LAUNDRY ===")
    #     if not data_member:
    #         print("Belum ada member terdaftar.")
    #     else:
    #         for i, member in enumerate(data_member, 1):
    #             print(f"{i}. {member}")
    #     enter()
    # case 4:
    #     clear()
    #     header()
    #     # lihat_riwayat()
    #     enter()
    # case 5:
    #     clear()
    #     header()
    #     # about()
    #     enter()
    # case 6:
    #     clear()
    #     header()
    #     print("\nTerima kasih telah menggunakan SIMATRI.")
    #     enter()
    case _:
        print("\nPilihan tidak valid.")
        enter()

data_pelanggan_kiloan()
data_pelanggan_satuan()
