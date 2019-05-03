# Soal 2 - Membalik Posisi Elemen List

x = []

def balikPosisi(x):
    y = []
    for i in range(len(x)):
        y.append(x[len(x)-(i+1)])
    return y

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))