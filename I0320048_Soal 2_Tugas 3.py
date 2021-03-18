#soal nomer 2
biodata = {'Nama Lengkap':'Hilmy Muhammad Aqil',
           'Hobi':['bermain game','meraparasi iphone','membeli iphone'],
           'Sosmed':['instagram:hilmymaqil','line:hilmyaqil29',],
           'Lagu Kesukaan':['kerinduan-payung teduh','menuju senja-payung teduh'],
           'Makanan Favorit':['carbonara','indomie']}
#mengubah hobi
biodata['Hobi'][0] = 'pergi naik motor'
biodata['Sosmed'][0] ='whatsapp:081381929890'
    
#menghapus makanan favorit
del biodata['Hobi'][1]
del biodata['Hobi'][0]

#menambahkan hobi
biodata['Hobi'].append('merakit pc')
print(biodata)

