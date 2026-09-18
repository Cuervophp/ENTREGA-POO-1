from operation import Salario

horas = 48
valor_hora = 5000
porcentaje_retencion = 0.125

empleado = Salario(horas, valor_hora, porcentaje_retencion)

print("Salario bruto: $", empleado.calcular_salario_bruto())
print("Retención en la fuente: $", empleado.calcular_retencion())
print("Salario neto: $", empleado.calcular_salario_neto())