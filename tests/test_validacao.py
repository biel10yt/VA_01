import unittest
from app.validacao import validar_cpf

class TestValidarCPF(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("12345678909"))  # Exemplo fictício de CPF válido

    def test_cpf_invalido(self):
        self.assertFalse(validar_cpf("12345678900"))  # CPF inválido

    def test_cpf_com_caracteres_extras(self):
        self.assertTrue(validar_cpf("123.456.789-09"))  # CPF válido com pontuação

    def test_cpf_todos_iguais(self):
        self.assertFalse(validar_cpf("11111111111"))  # CPFs com todos os dígitos iguais são inválidos

    def test_cpf_curto(self):
        self.assertFalse(validar_cpf("12345"))  # CPF com menos de 11 dígitos é inválido

if __name__ == "__main__":
    unittest.main()