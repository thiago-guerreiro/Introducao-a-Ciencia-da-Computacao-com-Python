def conta_letras(frase, contar="vogais"):
    vogais = consoantes = 0
    mapaDeVogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    frase = frase.replace(" ", "")
    for i in range(len(frase)):
        caracter = frase[i]
        if caracter in mapaDeVogais:
            vogais += 1
        else:
            consoantes += 1
    return vogais if contar == 'vogais' else consoantes

def test_contaVogais():
    assert conta_letras('programamos em python') == 6

def test_contaConsoante():
    assert conta_letras('programamos em python', 'consoantes') == 13
