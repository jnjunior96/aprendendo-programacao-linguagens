def contador_letras(listapalavras):
    contador = []
    for x in listapalavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

lista = ['cachorro',' gato']
total_letras = contador_letras(lista)
print(total_letras)

contador_letras2 = lambda lista2: [len(x) for x in lista2]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras2(lista_animais))
soma = lambda a , b : a + b
print(soma(10,5))

calculadora = {
    'soma' : lambda a,b: a + b,
    'subtração': lambda a , b: a - b,
    'multiplicação': lambda a,b: a * b,
    'divisão': lambda a , b: a / b,
}
soma = calculadora['soma']
print('A soma é:  {}' .format(soma(10,5)))