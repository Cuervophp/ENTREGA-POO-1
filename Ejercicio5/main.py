from operation import Circulo

radio = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio)

print("Área:", circulo.calcular_area())
print("Longitud de la circunferencia:", circulo.calcular_circunferencia())