print('-' * 40)
print('Menampilkan status seseorang apakah masih anak kecil atau sudah sudah dewasa !')
print('-' * 40)

umur = int(input('Masukan Umur : '))
dewasa = umur >= 17
# print(f"Dewasa : {dewasa}")
if not dewasa:
  print('Anda Masih Anak-anak')
else:
  print('Anda Sudah Dewasa')