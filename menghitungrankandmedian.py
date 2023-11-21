print('-' * 25)
print('Mengecek Ranking !')
print('-' * 25)

rank = int(input('Masukan Ranking : '))
rata_rata = float(input('Masukan Rata-Rata : '))

# cek menggunakan and
if rank == 1 and rata_rata > 8:
  print('Anak Mendapatkan Hadiah')
else:
   print('Anak Tidak Mendapatkan Hadiah')

# cek menggunakan or
if rank == 1 or rata_rata > 8:
  print('Anak Mendapatkan Hadiah')
else:
   print('Anak Tidak Mendapatkan Hadiah')