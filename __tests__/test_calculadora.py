import pytest
from calc.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

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
    