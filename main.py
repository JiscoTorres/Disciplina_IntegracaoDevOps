class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def operacao_complexa(self, a, b):
        # BUG INTENCIONAL: deveria ser multiplicação (*)
        return a + b