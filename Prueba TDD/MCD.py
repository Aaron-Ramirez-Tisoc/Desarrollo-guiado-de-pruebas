
import unittest

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 56
num2 = 98

resultado = mcd(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es {resultado}")

def mcd_4_numeros(a, b, c, d):
    
    mcd_ab = mcd(a, b)
    
    mcd_abc = mcd(mcd_ab, c)
    
    mcd_abcd = mcd(mcd_abc, d)
    return mcd_abcd

# Ejemplo de uso
num3 = 24
num4 = 36
num5 = 48
num6 = 60

resultado2 = mcd_4_numeros(num3, num4, num5, num6)
print(f"El máximo común divisor de {num3}, {num4}, {num5} y {num6} es {resultado2}")

class TestOperaciones(unittest.TestCase):
    def test_mcd_4_numeros(self):
        esperado = 5
        actual = mcd_4_numeros(5,15,45,90)
        self.assertEqual(actual,esperado)
    
    def test_mcd_4_numeros(self):
        esperado = 3
        actual = mcd_4_numeros(30,21,108,12)
        self.assertEqual(actual,esperado)

    def test_mcd_4_numeros(self):
        esperado = 1
        actual = mcd_4_numeros(11,37,45,15)
        self.assertEqual(actual,esperado)

if __name__ == '__main__':
    unittest.main()
