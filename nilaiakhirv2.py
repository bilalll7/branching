print('-' * 25)
print('Mengecek Nilai Akhir V2 !')
print('-' * 25)

nilai_tugas = float(input('Masukan Nilai Tugas : '))
nilai_uts = float(input('Masukan Nilai UTS : '))
nilai_uas = float(input('Masukan Nilai UAS : '))

nilai_akhir = 0.30 * nilai_tugas + 0.30 * nilai_uts + 0.40 * nilai_uas

if nilai_akhir >= 80 and nilai_akhir <= 100:
  print(f"Nilai Akhir : {nilai_akhir:6.2f}")
  print('A')
  print('Sangat Baik')
elif nilai_akhir >= 68 and nilai_akhir < 80:
  print(f"Nilai Akhir : {nilai_akhir:6.2f}")
  print('B')
  print('Baik')
elif nilai_akhir >= 56 and nilai_akhir < 68:
  print(f"Nilai Akhir : {nilai_akhir:6.2f}")
  print('C')
  print('Cukup')
elif nilai_akhir >= 45 and nilai_akhir < 56:
  print(f"Nilai Akhir : {nilai_akhir:6.2f}")
  print('D')
  print('Kurang')
elif nilai_akhir >= 0 and nilai_akhir < 45:
  print(f"Nilai Akhir : {nilai_akhir:6.2f}")
  print('E')
  print('Sangat Kurang')