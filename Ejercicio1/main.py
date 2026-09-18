from operation import Edades

edad_juan = float(input("Ingrese la edad de Juan: "))

persona = Edades(edad_juan)

print("Edad de Juan:", persona.edad_juan)
print("Edad de Alberto:", persona.calcular_alberto())
print("Edad de Ana:", persona.calcular_ana())
print("Edad de la mamá:", persona.calcular_mama())