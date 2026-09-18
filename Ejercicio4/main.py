from operation import Numero

numero = float(input("Ingrese un número: "))

operacion = Numero(numero)

print("Cuadrado:", operacion.calcular_cuadrado())
print("Cubo:", operacion.calcular_cubo())