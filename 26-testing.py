'''
/*
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
 */
'''

# 13 FRIDAY

import datetime

def friday_13 (year: int, month: int) -> bool:
    try:
        return datetime.datetime(year, month, 13).weekday() == 4
    except:
        return False

# TESTS

def test_true_date():
    assert friday_13(2023, 1)
    print("TRUE DATE: PASSED")
    

def test_false_date():
    assert not friday_13(2023, 7)
    print("FALSE DATE: PASSED")

def test_invalid_year():
    assert not friday_13("2023",1)
    assert not friday_13("miguel",1)
    assert not friday_13(-2023,1)
    print("INVALID YEAR: PASSED")

def test_invalid_month():
    assert not friday_13(2023,"1")
    assert not friday_13(2023,"uno")
    assert not friday_13(2023,-1)
    print("INVALID MONTH: PASSED")

def test_invalid_data():
    assert not friday_13("Miguel","dp")
    print("INVALID DATA: PASSED")

test_true_date()
test_false_date()
test_invalid_year()
test_invalid_month()
test_invalid_data()