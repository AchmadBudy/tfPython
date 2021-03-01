# import library xlsxwriter untuk membuat file excel
import xlsxwriter

masukA = input("masukkan nama file pertama : ")

a = open(masukA+".txt", encoding="utf8")
a = a.read()
a = a.splitlines()

print("berhasil crawling document 1")

masukB = input("masukkan nama file Kedua : ")

b = open(masukB+".txt", encoding="utf8")
b = b.read()
b = b.splitlines()

print("berhasil crawling document 2")

masukC = input("masukkan nama file ketiga : ")

c = open(masukC+".txt", encoding="utf8")
c = c.read()
c = c.splitlines()

print("berhasil crawling document 3")

masukD = input("masukkan nama file keempat : ")

d = open(masukD+".txt", encoding="utf8")
d = d.read()
d = d.splitlines()

print("berhasil crawling document 4")

# res = [] 
# [res.append(x) for x in a if x not in res] 
gabung = a+b+c+d
gabunganNotDouble = [] 
[gabunganNotDouble.append(x) for x in gabung if x not in gabunganNotDouble] 

listA = []
listB = []
listC = []
listD = []

for pecah in gabunganNotDouble:
    currrent = 0
    for pecahB in a:
        if pecah == pecahB:
            currrent += 1
    listA.append(currrent)

for pecah in gabunganNotDouble:
    currrent = 0
    for pecahB in b:
        if pecah == pecahB:
            currrent += 1
    listB.append(currrent)

for pecah in gabunganNotDouble:
    currrent = 0
    for pecahB in c:
        if pecah == pecahB:
            currrent += 1
    listC.append(currrent)

for pecah in gabunganNotDouble:
    currrent = 0
    for pecahB in d:
        if pecah == pecahB:
            currrent += 1
    listD.append(currrent)


namaFile = input("masukkan nama file excelnya : ")
# memulai inisiasi pembuatan excelnya
workbook = xlsxwriter.Workbook('hasil/'+namaFile+'.xlsx')
# pembukaan worksheet baru
worksheet = workbook.add_worksheet()
# pembuatan daftar unik
row = 0
worksheet.write(row, 0, "Daftar Unik Token")
for col, data in enumerate([gabunganNotDouble]):
            worksheet.write_column(row+1, 0, data)

row = 0
worksheet.write(row, 1, "Daftar di DOcument 1")
for col, data in enumerate([listA]):
            worksheet.write_column(row+1, 1, data)

row = 0
worksheet.write(row, 2, "Daftar di DOcument 2")
for col, data in enumerate([listB]):
            worksheet.write_column(row+1, 2, data)

row = 0
worksheet.write(row, 3, "Daftar di DOcument 3")
for col, data in enumerate([listC]):
            worksheet.write_column(row+1, 3, data)

row = 0
worksheet.write(row, 4, "Daftar di DOcument 4")
for col, data in enumerate([listD]):
            worksheet.write_column(row+1, 4, data)


workbook.close()

print("File sudah jadi silahkan di ambil di ")
