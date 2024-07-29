from django.test import TestCase
from rest_framework.test import APIRequestFactory
from selenium.webdriver import Firefox

# Testes de Filipe de Oliveira Ataíde

# Teste Unitário

class UnitarioCadastroTestCase(TestCase):
    def test_unitario_cadastro(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/',
        {
            'username': 'usuario_test',
            'email': 'usuario_test@mail.com',
            'first_name': 'Usuario',
            'last_name': 'Teste',
            'password': 're12345678',
            're_password': 're12345678'
        })
        return request

# Testes de sistema

class SistemaCadastroTestCase(TestCase):
    def test_sistema_cadastro(self):
        self.driver = Firefox()
        self.driver.get("http://localhost:8080/Cadastro")
        self.driver.find_element_by_name("username").send_keys("testecookit")
        self.driver.find_element_by_name("first_name").send_keys("Teste")
        self.driver.find_element_by_name("last_name").send_keys("CookIt")
        self.driver.find_element_by_name("password").send_keys("re12345678")
        self.driver.find_element_by_name("email").send_keys("teste@cookit.com")
        self.driver.find_element_by_name("re_password").send_keys("re12345678")
        self.driver.find_element_by_name("submit_form").click()

class SistemaLoginTestCase(TestCase):
    def test_sistema_login(self):
        self.driver = Firefox()
        self.driver.get("http://localhost:8080/Login")
        self.driver.find_element_by_name("email").send_keys("teste@cookit.com")
        self.driver.find_element_by_name("password").send_keys("re12345678")
        self.driver.find_element_by_name("submit_form").click()

# Teste de Integração

class IntegracaoTestCase(TestCase):
    def test_cadastro(self):
        self.driver = Firefox()
        self.driver.get("http://localhost:8080/Cadastro")

        self.driver.find_element_by_name("first_name").send_keys("Teste")
        self.driver.find_element_by_name("last_name").send_keys("CookIt")
        self.driver.find_element_by_name("username").send_keys("testecookit")
        self.driver.find_element_by_name("email").send_keys("teste@cookit.com")
        self.driver.find_element_by_name("password").send_keys("re12345678")
        self.driver.find_element_by_name("re_password").send_keys("re12345678")
        self.driver.find_element_by_name("submit_form").click()

        self.driver.get("http://localhost:8080/Login")
        
        self.driver.find_element_by_name("email").send_keys("teste@cookit.com")
        self.driver.find_element_by_name("password").send_keys("re12345678")
        self.driver.find_element_by_name("submit_form").click()