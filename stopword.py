# import library xlsxwriter untuk membuat file excel
import xlsxwriter


# membuat class guna mempermudah hidup
class autoRIS:
    # Inisiasi awal class
    def __init__(self,namaExcel,namaTxt):
        # deklarasi nama excelnya
        self.workbook = xlsxwriter.Workbook(namaExcel+".xlsx")
        # pembukaan worksheet baru
        self.worksheet = self.workbook.add_worksheet() 
        # nama txt   
        self.namaTxt = namaTxt+".txt"
    
    def mulai(self):
        f = open(self.namaTxt, encoding="utf8")
        a = f.read()
        a = a.split()
        array = [a]
        row = 0
        self.worksheet.write(row, 0, "Daftar Tokenizing")
        for col, data in enumerate(array):
            self.worksheet.write_column(row+1, 0, data)
        
        # memulai stopword
        fileStop = open("stopword.txt", "r")
        fileStop = fileStop.read()
        fileStop = fileStop.split()
        k = []
        for z in fileStop :
            for x in a:
                if z == x.lower():
                    k.append(x)
        res = [] 
        [res.append(x) for x in k if x not in res] 

        array = [res]
        row = 0
        self.worksheet.write(row, 4, "Daftar Stop Listnya")
        for col, data in enumerate(array):
            self.worksheet.write_column(row+1, 4, data)

        awal = 0
        total = 0
        for x in a:
            for y in res:
                if x.lower() == y:
                    a[awal]="geovani"
                    total += 1
            awal+=1
        array = [a]
        kata = "Terdapat {} stopword dalam document"
        print(kata.format(total))
        row = 0
        print("File Sudah Terbaguskan juga")
        self.worksheet.write(row, 3, "Hasil Stop Listnya")
        for col, data in enumerate(array):
            self.worksheet.write_column(row+1, 3, data)
        self.workbook.close()
        print("File Sudah Terbuat dengan baik dan benar")

        
    

x = input("Masukkan Nama Excel buat nanti dibuat : ")
y = input("masukkan nama txt nya target awalanya : ")
autoRIS(x,y).mulai()
