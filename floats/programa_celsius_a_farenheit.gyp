#Celsius a Farenheit
def celsiusAFarenheit(gradosC):
  if gradosC > 0:
    gradosF = ((gradosC*9/5)+32)
    print (gradosF)
  else:
    print("Error")
celsiusAFarenheit(gradosC=float(input("Ingrese la temperatura en grados Celsius:")))
