#Celsius a Kelvin
def celsiusAKelvin(gradosC):
  if gradosC > 0:
    gradosK = (gradosC+273,15)
    print (gradosK)
  else:
    print("Error")
celsiusAKelvin(gradosC=float(input("Ingrese la temperatura en grados Celsius:")))
