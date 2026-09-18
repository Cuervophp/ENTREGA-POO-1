class Salario:

    def __init__(self, horas, valor_hora, porcentaje_retencion):
        self.horas = horas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self):
        return self.horas * self.valor_hora

    def calcular_retencion(self):
        return self.calcular_salario_bruto() * self.porcentaje_retencion

    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() - self.calcular_retencion()