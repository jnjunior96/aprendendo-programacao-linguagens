# Função retorna um valor, metodo não retorna
#médtodo significa definição DEF
from msilib.schema import Class
from typing_extensions import Self
# def soma(a, b):
#     return a +b
# print(soma(23, 20))
# print(soma(100, 100))

# def subtracao(a, b):
#     return a - b
# print(subtracao(23, 20))
# print(subtracao(100, 100))

#classe
# class Calculadora:
#     def soma(self, valor_a , valor_b):
#         return valor_a + valor_b
#     def subtracao(self, valor_a, valor_b):
#         return valor_a - valor_b
# calc = Calculadora()
# print(Calculadora.soma(10,2))
# print(Calculadora.subtracao(10,2))

class Televisao:
    def __init__(self):
        Self.ligada = False
        Self.canal = 5
    def power(self):
        if Self.ligada:
            Self.ligada = False
        else:
            Self.ligada = True
    def aumenta_canal(self):
        if Self.ligada:
            Self.canal +=1
    def diminui_canal(self):
        if Self.ligada:
            Self.canal -=1
televisao = Televisao()
print('Televisão está ligada : {}'.format(televisao))



