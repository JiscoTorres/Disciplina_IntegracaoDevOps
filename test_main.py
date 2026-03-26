from main import Calculadora

def test_operacao_complexa_deve_multiplicar():
    calc = Calculadora()
    resultado = calc.operacao_complexa(2, 5)
    assert resultado == 10