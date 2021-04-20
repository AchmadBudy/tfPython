# import library xlsxwriter untuk membuat file excel
import xlsxwriter

# memulai inisiasi pembuatan excelnya
# buat nama excelnya
workbook = xlsxwriter.Workbook('percobaan.xlsx')
# pembukaan worksheet baru
worksheet = workbook.add_worksheet()
# buat targetnya
f = open("aa.txt", encoding="utf8")
a = f.read()
a = a.split()
array = [a]

row = 0

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()
