#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class Calculater:
    def __init__(self, celsius) -> None:
        self.celsius = celsius
  
    def celsius_para_fahrenheit(self):
        return self.celsius * 1.8 + 32

# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:

conversor = Calculater(celsius=celsius)
resultado = conversor.celsius_para_fahrenheit()
print(resultado)