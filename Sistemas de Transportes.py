# Classe base
class Transporte:
    def mover(self):
        return "O transporte está se movendo..."

# Classes filhas
class Carro(Transporte):
    def mover(self):
        return "O carro está rodando pela estrada."

class Moto(Transporte):
    def mover(self):
        return "A moto está acelerando."

class Bicicleta(Transporte):
    def mover(self):
        return "A bicicleta está pedalando."

# Programa principal
def main():
    # Lista com diferentes transportes
    transportes = [Carro(), Moto(), Bicicleta()]

    # Polimorfismo: mesmo método, comportamentos diferentes
    for t in transportes:
        print(t.mover())

# Executa o programa
main()
