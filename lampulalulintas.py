print('-' * 25)
print('Mengecek Lampu lalu lintas !')
print('-' * 25)

warna = input('Masukan Warna Lampu Lalu Lintas : ').upper()

if warna == 'HIJAU':
  print('Silahkan Jalan !')
elif warna == 'KUNING':
  print('Siap - Siap !')
elif warna == 'MERAH':
  print('Berhenti !')
else:
  print('Warna Tidak dikenal')