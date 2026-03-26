from main import Calculadora

def test_operacao_complexa_deve_multiplicar():
    calc = Calculadora()
    resultado = calc.operacao_complexa(2, 5)
    # Espera 10, mas o código retorna 7 (bug!)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"