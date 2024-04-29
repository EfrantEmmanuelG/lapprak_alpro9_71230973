def tiga_tertinggi(data):
    urut = sorted(data, reverse=True)
    nilai_terbaik = urut[:3]
    return nilai_terbaik

data = [90,57,98,65,99,76,88,85,97,95]

print(tiga_tertinggi(data))