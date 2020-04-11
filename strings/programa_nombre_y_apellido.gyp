#Mini-desafío: Operaciones con strings

nombre=input('Ingrese su nombre: ')
apellido=input('Ingrese su apellido: ')

nombre_y_apellido = nombre + ' ' + apellido

if len(nombre_y_apellido) < 26:
  print('Nombre admitido:', nombre_y_apellido)
else:
  print('Nombre no admitido:',nombre[0:1], apellido[0:24])
