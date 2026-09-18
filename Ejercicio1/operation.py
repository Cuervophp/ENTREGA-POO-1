class Edades:

    def __init__(self, edad_juan):
        self.edad_juan = edad_juan

    def calcular_alberto(self):
        return (2 / 3) * self.edad_juan

    def calcular_ana(self):
        return (4 / 3) * self.edad_juan

    def calcular_mama(self):
        return self.edad_juan + self.calcular_alberto() + self.calcular_ana()