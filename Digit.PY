def digitAwal(angka1,angka2):
    hasil = angka1 ** angka2 #rumus matematika pangkat berdasarkan 2 parameter
    list_hasil =list(str(hasil)) #merubah variable hasil yang sebelumnya integer menjadi string lalu masuk kedalam list
    return (list_hasil[0]) #menggunakan access data list utk mengambil digit awal


print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))

def digitAkhir(angka1,angka2):
    hasil = angka1 ** angka2 #rumus matematika pangkat berdasarkan 2 parameter
    list_hasil =list(str(hasil)) #merubah variable hasil yang sebelumnya integer menjadi string lalu masuk kedalam list
    return (list_hasil[-1]) #menggunakan access data list utk mengambil digit akhir


print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))

