def mencari_min_max():
    angka = []
    while True:
        data = input("Masukkan angka (ketik 'done' untuk selesai): ")
        
        if data.lower() == 'done':
            break
        
        try:
            nomor = float(data)
            angka.append(nomor)
        except ValueError:
            print("Input tidak valid.")

    if angka:
        print("Nilai maksimum:", max(angka))
        print("Nilai minimum:", min(angka))
    else:
        print("Tidak ada angka yang dimasukkan.")

if __name__ == "__main__":
    mencari_min_max()

