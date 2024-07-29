from django.test import TestCase

from .models import Receita
from selenium import webdriver
from selenium.webdriver import Firefox
from rest_framework.test import APIRequestFactory 

from receita.models import Receita, Ingrediente
from usuario.models import User

# Create your tests here.

# Teste Unitário CRUD receita por sessão -  Silva

'''
class SessionTest(TestCase):
    def test_session_create(self):
        factory = APIRequestFactory()
        ingredientes = [
            {
                'nome_ingrediente': 'chocolate',
                'unidade_medida_ingrediente': 'U',
                'quantidade_ingrediente': 1
            }
        ]
        request = factory.post('api/post-receita',
        {   
            'nome_receita': 'ovo de pascoa', 
            'modo_preparo': 'Esquente o chocolate',
            'porcoes': 2,
            'sabor_receita': 'D',
            'tempo_preparo': 4,
            'tempo_unidade_medida': 'M',
            'categoria': 'A',
            'dificuldade': 'M', 
            'observacoes_adicionais': 'comentário',
            'dono_receita': 1,
            'ingredientes': ingredientes
        })
        return request
    
    def test_session_view(self):
        factory = APIRequestFactory()
        request = factory.get('api/receita')
        
        return request


    def test_session_update(self):
        
        factory = APIRequestFactory()
        ingredientes = [
            {
                'nome_ingrediente': 'chocolate',
                'unidade_medida_ingrediente': 'U',
                'quantidade_ingrediente': 5
            }
        ]

        request = factory.put('api/post-receita/1',
        {   
            'nome_receita': 'ovo de pascoa', 
            'modo_preparo': 'chocolate',
            'porcoes': 2,
            'sabor_receita': 'D',
            'tempo_preparo': 4,
            'tempo_unidade_medida': 'M',
            'categoria': 'A',
            'dificuldade': 'M', 
            'observacoes_adicionais': 'comentário',
            'dono_receita': 1,
            'ingredientes': ingredientes
        })

        return request

    def test_session_delete(self):
        factory = APIRequestFactory()
        request = factory.delete('api/receita/1')
        
        return request
'''
'''
# Teste de sistemas CRUD por sessão -  Silva

class create_user(TestCase):
    def test_login_session(self):
        self.driver = Firefox()
        self.driver.get('http://localhost:8080/Login')
        self.driver.find_element_by_name('email').send_keys("luan@gmail.com")
        self.driver.find_element_by_name('password').send_keys("meteorodapaixao")
        self.driver.find_element_by_name('submit_form').click()


    def test_cadastro_session(self):
        self.driver = Firefox()
        self.driver.get('http://localhost:8080/FormReceita/')
        self.driver.find_element_by_name('nome_receita').send_keys("ovo de pascoa")
        # self.driver.find_element_by_name('categoria').send_keys("L")
        # self.driver.find_element_by_name('sabor_receita').send_keys("D")
        # self.driver.find_element_by_name('dificuldade').send_keys("M")
        self.driver.find_element_by_name('porcoes').send_keys(2)
        self.driver.find_element_by_name('tempo_preparo').send_keys(50)
        # self.driver.find_element_by_name('tempo_unidade_medida').send_keys("M")
        self.driver.find_element_by_name('ingrediente').send_keys("chocolate")
        self.driver.find_element_by_name('add-button').click()
        self.driver.find_element_by_name('quantidade_ingrediente').send_keys(5)
        # self.driver.find_element_by_name('unidade_medida_ingrediente').send_keys("U")
        self.driver.find_element_by_name('modo_preparo').send_keys("Esquente o chocolate")
        self.driver.find_element_by_name('observacoes_adicionais').send_keys("comentário")
        self.driver.find_element_by_name('submit-button').click()

    def test_list_session(self):
        self.driver = Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('button-detail').click()
    
    def test_update_session(self):
        self.driver = Firefox()
        self.driver.get("http://localhost:8080/EditarReceita/1")
        self.driver.find_element_by_name('nome_receita').send_keys("ovo de pascoa trunfado")
        self.driver.find_element_by_name('submit-button').click()
'''

'''
Victor Augusto Fernandes Pereira - 20172014040022

Teste de sistema:

class IserirReceitaSelenium(TestCase):    
    def test_criar_receita_selenium(self):
        #driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
       
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        
        self.driver.get('http://localhost:8080/FormReceita')
        
        self.driver.find_element_by_name('nr').send_keys("teste1")
        
        self.driver.find_element_by_name('ingre').send_keys("t1")
        
        self.driver.find_element_by_id("unidade-medida").send_keys("CH")
        
        self.driver.find_element_by_name('qtdi').send_keys("5")
        
        self.driver.find_element_by_name('btaddr').click()
        
        self.driver.find_element_by_name('ctgr').send_keys("Lanche")
        
        self.driver.find_element_by_name('mp').send_keys("Null")
        
        self.driver.find_element_by_id("rbdoce").click()
        
        self.driver.find_element_by_id('portions').send_keys("1")
        
        self.driver.find_element_by_id('prep-time').send_keys("1")
        
        self.driver.find_element_by_id("difficulty").send_keys("D")
        
        self.driver.find_element_by_name('oad').send_keys("null")

        self.driver.find_element_by_id('submit-button').click()

        #self.driver=Edge()
        #self.driver.get('http://localhost:8080/')
        #self.driver.find_element_by_id("//input[@value='D']").click()


#Teste Unitario
from rest_framework.test import APIRequestFactory

class InserirReceita(TestCase):     
    
    def test_criar_receita1(self):
        factory = APIRequestFactory()
        ingredientes = [{
            'nome_ingrediente':'Teste',
            'unidade_medida_ingrediente':'Xicara',  
            'quantidade_ingrediente':'2',
        }]
        request = factory.post('api/post-receita',{    
            'nome_receita':'teste1',
            'modo_preparo':'null',
            'porcoes':'2',
            'sabor_receita':'D',
            'tempo_preparo':'2',
            'tempo_unidade_medida':'H',
            'dono_receita':'1',
            'fotos':'',
            'categoria':'A',
            'dificuldade':'D',
            'data_publicacao':'',
            'observacoes_adicionais':'Null',
            'ingrediete': ingredientes,
        })
        return request

class InserirReceita1(TestCase):
    def test_criar_receita2(self):
        factory = APIRequestFactory()
        ingredientes = [{
            'nome_ingrediente':'Teste',
            'unidade_medida_ingrediente':'Xicara',  
            'quantidade_ingrediente':'2',
        }]
        request = factory.post('api/post-receita',{    
            'nome_receita':'',
            'modo_preparo':'null',
            'porcoes':'2',
            'sabor_receita':'D',
            'tempo_preparo':'2',
            'tempo_unidade_medida':'',
            'dono_receita':'1',
            'fotos':'',
            'categoria':'A',
            'dificuldade':'',
            'data_publicacao':'',
            'observacoes_adicionais':'Null',
            'ingrediete': ingredientes,
        })
        return request


class InserirReceita2(TestCase):
        def test_criar_receita2(self):
            factory = APIRequestFactory()
            ingredientes = [{
                'nome_ingrediente':'',
                'unidade_medida_ingrediente':'',  
                'quantidade_ingrediente':'',
            }]
            request = factory.post('api/post-receita',{    
                'nome_receita':'',
                'modo_preparo':'',
                'porcoes':'',
                'sabor_receita':'',
                'tempo_preparo':'',
                'tempo_unidade_medida':'',
                'dono_receita':'',
                'fotos':'',
                'categoria':'',
                'dificuldade':'',
                'data_publicacao':'',
                'observacoes_adicionais':'',
                'ingrediete': ingredientes,
            })
            return request

'''
# Feitos por Alanis Isabelle de Oliveira Silva

# Create your tests here. WIP

class BuscaTestCase(TestCase):
    def setUp(self):
        Cookinho = User.objects.create(username="CookIt", first_name="Cook", last_name="It", password="cookit")

        X = Ingrediente.objects.create(nome_ingrediente="X", unidade_medida_ingrediente="U", quantidade_ingrediente=1)
        Y = Ingrediente.objects.create(nome_ingrediente="Y", unidade_medida_ingrediente="U", quantidade_ingrediente=1)

        C1 = [
                X
            ]
        C2 = [
                Y
            ]

        RA = Receita.objects.create(
            dono_receita=Cookinho,
            nome_receita="Biscoito",
            modo_preparo="?",
            porcoes=1,
            sabor_receita="D",
            tempo_preparo=1,
            tempo_unidade_medida="M",
            categoria="A",
            dificuldade="F",
            observacoes_adicionais="?",
            )
        RA.ingredientes.set(C1)

        RB = Receita.objects.create(
            dono_receita=Cookinho,
            nome_receita="Bolo",
            modo_preparo="?",
            porcoes=1,
            sabor_receita="D",
            tempo_preparo=1,
            tempo_unidade_medida="M",
            categoria="B",
            dificuldade="F",
            observacoes_adicionais="?",
            )
        RB.ingredientes.set(C2)

    def test_ingrediente_X(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=&categoria__in=&ingredientes__nome_ingrediente__in=X&ingredientes_not=')
        return request

    def test_ingrediente_Y(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=&categoria__in=&ingredientes__nome_ingrediente__in=Y&ingredientes_not=')
        return request

    def test_ingrediente_nao_ter_Y(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=&categoria__in=&ingredientes__nome_ingrediente__in=&ingredientes_not=Y')
        return request
    #
    def test_ingrediente_X_e_Y(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=&categoria__in=&ingredientes__nome_ingrediente__in=X%2CY&ingredientes_not=')
        return request

    def test_ingrediente_Y_e_nao_ter_Y(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=&categoria__in=&ingredientes__nome_ingrediente__in=Y&ingredientes_not=Y')
        return request

    def test_ingrediente_X_e_nao_ter_Y(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=&categoria__in=&ingredientes__nome_ingrediente__in=X&ingredientes_not=Y')
        return request
#     ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    def test_dificuldade_F(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=F&categoria__in=&ingredientes__nome_ingrediente__in=&ingredientes_not=')
        return request

    def test_dificuldade_F_nao_ter_Y(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=F&categoria__in=&ingredientes__nome_ingrediente__in=&ingredientes_not=Y')
        return request

    def test_dificuldade_F_ingrediente_X_nao_ter_Y(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=F&categoria__in=&ingredientes__nome_ingrediente__in=X&ingredientes_not=Y')
        return request

#     ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    def test_tipo_doce(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=doce&dificuldade=F&categoria__in=&ingredientes__nome_ingrediente__in=&ingredientes_not=')
        return request

    def test_tipo_salgado(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=salgado&dificuldade=F&categoria__in=&ingredientes__nome_ingrediente__in=&ingredientes_not=')
        return request

#     ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    def test_categoria_B(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=&categoria__in=B&ingredientes__nome_ingrediente__in=&ingredientes_not=')
        return request

    def test_categoria_A_B(self):
        factory = APIRequestFactory()
        request = factory.get('/api/receita/?nome_receita__icontains=&sabor_receita__in=&dificuldade=&categoria__in=A%2C+B&ingredientes__nome_ingrediente__in=&ingredientes_not=')
        return request

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Busca simples

class BuscaSelTestCase(TestCase):
    def test_busca_simples_nome_X(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('search-input').send_keys('X')
        self.driver.find_element_by_name('search-button').click()

# -------------------------------------------------------------------------------------------------------
# Busca Avançada

class BuscaAvancadaTestCase(TestCase):
    
    def test_BuscaAvancada_ingrediente_X(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('querotenha').send_keys('X')
        self.driver.find_element_by_name('bts1').click()
    
    def test_BuscaAvancada_ingrediente_X(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('querotenha').send_keys('X')
        self.driver.find_element_by_name('bts1').click()

    def test_BuscaAvancada_ingrediente_Y(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('querotenha').send_keys('Y')
        self.driver.find_element_by_name('bts1').click()

    def test_BuscaAvancada_ingrediente_nao_ter_Y(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('queronaotenha').send_keys('Y')
        self.driver.find_element_by_name('bts2').click()
    
    def test_BuscaAvancada_ingrediente_X_Y(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('querotenha').send_keys('X')
        self.driver.find_element_by_name('bts1').click()
        self.driver.find_element_by_name('querotenha').send_keys('Y')
        self.driver.find_element_by_name('bts1').click()
    
    def test_BuscaAvancada_ingrediente_Y_e_nao_ter_Y(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('querotenha').send_keys('Y')
        self.driver.find_element_by_name('bts1').click()
        self.driver.find_element_by_name('queronaotenha').send_keys('Y')
        self.driver.find_element_by_name('bts2').click()
 
    def test_ingrediente_X_e_nao_ter_Y(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('querotenha').send_keys('X')
        self.driver.find_element_by_name('bts1').click()
        self.driver.find_element_by_name('queronaotenha').send_keys('Y')
        self.driver.find_element_by_name('bts2').click()
    ###
    ####WIP#####
    '''
    def test_BuscaAvancada_dificuldade_F(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_id('input-23').click
        #self.driver.execute_script("arguments[Fácil].choice;", select) 
    
    def test_BuscaAvancada_dificuldade_F_nao_ter_Y(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('difficult').input(F)
        self.driver.find_element_by_name('queronaotenha').send_keys('Y')
        self.driver.find_element_by_name('bts2').click()

    def test_BuscaAvancada_dificuldade_F_ingrediente_X_nao_ter_Y(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_name('difficult').input(F)
        self.driver.find_element_by_name('querotenha').send_keys('X')
        self.driver.find_element_by_name('bts1').click()
        self.driver.find_element_by_name('queronaotenha').send_keys('Y')
        self.driver.find_element_by_name('bts2').click()
    '''
#   ---------------------------------------------------------------------------------------------------------------------------------------------------------------
        ########AJUDAAA########
        #python manage.py test receita.tests.BuscaAvancadaTestCase.test_BuscaAvancada_tipo_doce 
    def test_BuscaAvancada_tipo_doce(self):
        self.driver=Firefox()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/')
        #self.driver.find_element_by_name('Doce').click() #Funciona obstruido
        #self.driver.find_element_by_id('input-28').click() #Funciona obstruido
        #self.driver.find_element_by_xpath("//input[@value='D']").click() 
        element = self.driver.find_element_by_xpath("//input[@value='D']")
        self.driver.execute_script("arguments[0].click();", element)   

    def test_BuscaAvancada_tipo_salgado(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        element = self.driver.find_element_by_xpath("//input[@value='S']")
        self.driver.execute_script("arguments[0].click();", element)
        
#     ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    def test_BuscaAvancada_categoria_B(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        element = self.driver.find_element_by_xpath("//input[@value='B']")
        self.driver.execute_script("arguments[0].click();", element)

    def test_BuscaAvancada_categoria_A_B(self):
        self.driver=Firefox()
        self.driver.get('http://localhost:8080/')
        element1 = self.driver.find_element_by_xpath("//input[@value='A']")
        self.driver.execute_script("arguments[0].click();", element1)
        element2 = self.driver.find_element_by_xpath("//input[@value='B']")
        self.driver.execute_script("arguments[0].click();", element2)




