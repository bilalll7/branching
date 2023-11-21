print('-' * 25)
print('Menghitung Penjualan Barang !')
print('-' * 25)

harga = int(input('Masukan Harga Barang : '))
qty = int(input('Masukan Qty : '))

subtotal = harga * qty
if qty >= 12:
  diskon = 0.20 * subtotal
else:
  diskon = 0

total_bayar = subtotal -  diskon
print(f"Sub Total    : Rp. {subtotal:10}")
print(f"Diskon       : Rp. {diskon:10.0f}")
print(f"Total Bayar  : Rp. {total_bayar:10.0f}")
