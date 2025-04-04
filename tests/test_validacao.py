import unittest
from app.validacao import validar_cpf

class TestValidarCPF(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("12345678909")) 
    def test_cpf_invalido(self):
        self.assertFalse(validar_cpf("12345678900"))

    def test_cpf_com_caracteres_extras(self):
        self.assertTrue(validar_cpf("123.456.789-09"))

    def test_cpf_todos_iguais(self):
        self.assertFalse(validar_cpf("11111111111"))

    def test_cpf_curto(self):
        self.assertFalse(validar_cpf("12345"))
        
if __name__ == "__main__":
    unittest.main()