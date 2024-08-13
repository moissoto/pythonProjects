def test_operacion():
    # Test case for addition
    assert operacion(5, 3, 1) == 8

    # Test case for subtraction
    assert operacion(10, 4, 2) == 6

    # Test case for multiplication
    assert operacion(2, 6, 3) == 12

    # Test case for division
    assert operacion(10, 2, 4) == 5

    # Test case for division by zero
    assert operacion(10, 0, 4) == 'Aritmetica no válida. No se puede dividir entre 0.'

    # Test case for modulo
    assert operacion(7, 3, 5) == 1

test_operacion()