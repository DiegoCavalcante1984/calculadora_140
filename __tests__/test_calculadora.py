import pytest
from calc.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, dividir_por_zero
from utils.utils import ler_csv

# padrão / standard AAA (se diz Tliple A)=Arrange,Act,Assert

def test_somar_dois_numeros():


    #Arrange/prepara/configura
    #Dados de saída
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    #Act / Executa

    resultado_obtido = somar_dois_numeros(num1, num2)

    #Acert /Valida
    assert resultado_esperado == resultado_obtido

def test_subtarir_dois_numeros():

    num1 = 7
    num2 = 5
    resultado_esperado = 2

    resultado_obtido = subtrair_dois_numeros(num1,num2)    

    assert resultado_esperado == resultado_obtido


def test_multiplicar_dois_numeros():

    num1 = 7
    num2 = 5
    resultado_esperado = 35

    resultado_obtido = multiplicar_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

def test_divir_dois_numeros():

    num1 = 10
    num2 = 2
    resultado_esperado = 5

    resultado_obtido = dividir_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

def test_dividir_por_zero():
    num1 = 10
    num2 = 0
    resultado_esperado = 'ERRO : Não e possivel dividir por zero'  

    resultado_obtido = dividir_por_zero(num1, num2)

    assert resultado_esperado == resultado_obtido

#---------------------------------------------------------------------------


# Testes baseados em dados /Date driven tests(DDT)
# Dados em uma lista
# Dados em um arquivo
# Varios formatos:csv(texto separado por vírgula),json,xml,dat


@pytest.mark.parametrize('num1, num2, resultado_esperado',
                         [
                           (5,7,12),
                           (0,8,8),
                           (10,-15,-5),
                           (6,0.75,6.75)   
                         ]
                         )


def test_somar_dois_numeros_lista(num1,num2,resultado_esperado):


    #Arrange/prepara/configura
    #Dados de saída fornecidos pela massa de teste em formato de lista

    

    #Act / Executa

    resultado_obtido = somar_dois_numeros(num1, num2)

    #Acert /Valida
    assert resultado_esperado == resultado_obtido   



#===========================================================
@pytest.mark.parametrize('num1,num2,resultado_esperado',
                         ler_csv("./fixtures/massa_somar.csv")
                         )
def test_somar_dois_numeros_csv(num1,num2,resultado_esperado):


    #Arrange/prepara/configura
    #Dados de saída fornecidos pela massa de teste em formato de lista

    

    #Act / Executa

    resultado_obtido = somar_dois_numeros(float(num1), float(num2))

    #Acert /Valida
    assert float(resultado_esperado) == resultado_obtido       