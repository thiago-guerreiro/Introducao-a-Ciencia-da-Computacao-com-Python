def primeiro_lex(lista):
    if not len(lista) or type(lista) != list:
        return False
    primeiroString = lista[0]
    for s in lista:
        if s < primeiroString:
            primeiroString = s
    return primeiroString

def test_OrdemLexicografica():
    lista = ['oĺá', 'A', 'a', 'casa']
    assert primeiro_lex(lista) == "A"

def test_listaVazia():
	lista = []
	assert primeiro_lex(lista) == False

def test_listaInvalida():
	lista = "maça banana laranja"
	assert primeiro_lex(lista) == False
