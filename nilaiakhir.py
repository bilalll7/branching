print('-' * 25)
print('Menghitung Nilai Akhir !')
print('-' * 25)


nilai_uts = int(input('Masukan Nilai UTS : '))
nilai_uas = int(input('Masukan Nilai UAS : '))
nilai_akhir = 0.40 * nilai_uts + 0.60 * nilai_uas

print(f"Nilai Akhir : {nilai_akhir:6.2f}")
if nilai_akhir == 100:
  print('>>> Sempurna ! <<<')