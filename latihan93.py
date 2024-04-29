def mengubah_text(file):
    with open(file, 'r') as f:
        kata = f.readlines()
        print('==================ISI BERITA==================')
        print(kata)
        print('==================Kata unik pada berita==================')
        for line in kata:
            list = line.strip().split()
            print(list)

namafile = "beritagempa.txt"
mengubah_text(namafile)