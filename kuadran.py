print('-' * 25)
print('Menentukan lokasi kuadran suatu koordinat !')
print('-' * 25)

x = int(input('Masukan Koordinat Titik X : '))
y = int(input('Masukan Koordinat Titik Y : '))

if x > 0 and y > 0:
  print('Koordinat (',x,',',y,') berada di kuadran I')
elif x < 0 and y > 0:
  print('Koordinat (',x,',',y,') berada di kuadran II')
elif x < 0 and y < 0:
  print('Koordinat (',x,',',y,') berada di kuadran III')
elif x > 0 and y < 0:
  print('Koordinat (',x,',',y,') berada di kuadran IV')
elif x == 0 and y == 0:
  print('Koordinat (',x,',',y,') berada di Titik Pusat')
elif x == 0 and y != 0:
  print('Koordinat (',x,',',y,') berada di Sumbu X')
elif x != 0 and y == 0:
  print('Koordinat (',x,',',y,') berada di Sumbu Y')
