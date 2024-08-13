def test_operacion():
    assert operacion(2, 3, 1) == 5
    assert operacion(5, 2, 2) == 3
    assert operacion(4, 6, 3) == 24
    assert operacion(10, 2, 4) == 5.0
    assert operacion(7, 3, 5) == 1

def test_calculadora():
    assert calculadora(1) == None
    assert calculadora(2) == None
    assert calculadora(3) == None
    assert calculadora(4) == None
    assert calculadora(5) == None
    assert calculadora(6) == None

test_operacion()
test_calculadora()