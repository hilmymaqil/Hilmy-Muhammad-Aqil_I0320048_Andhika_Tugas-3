#Tugas no 1 prongkom minggu 3

#list 10 konco dulur
konco = ['ilham','fairuz','fasya','tasya','yayuk',
         'kinor','azzam','dio','maul','maman']

#menampilkan isi list temen no 4,6,7
print(konco[4])
print(konco[6])
print(konco[7])

#Ganti nama konco list 3 5 9
konco[3] = 'nadhira'
konco[5] = 'noor'
konco[9] = 'fadhila'
print(konco)

#Menambah 2 nama konco
konco.append('juminem')
konco.append('kolluy')
print(konco)

#menampilkan semua teman dengan perulangan
for i in konco:
    print('{}' .format (i))
