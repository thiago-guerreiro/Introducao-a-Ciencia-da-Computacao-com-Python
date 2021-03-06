import re

def le_assinatura():
    print("")
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    
    while texto:
        textos.append(texto)
        i += 1
        print()
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)



def total_caracteres(lista):
    total_caracter = 0
    
    for i in range(0, len(lista)):
        total_caracter = total_caracter + len(lista[i])

    return total_caracter

def compara_assinatura(as_a, as_b):
    similaridade = 0
    
    for i in range(0, 6):
        positivo = as_a[i] - as_b[i]
        if positivo < 0:
            positivo = positivo * -1
        similaridade = similaridade + positivo
    similaridade_final = similaridade / 6
    return similaridade_final

def calcula_assinatura(texto):
    lista_sentencas = separa_sentencas(texto)
    total_frase = 0
    lista_frase = []
    
    for sentenca in lista_sentencas:
        lista_frase = lista_frase + separa_frases(sentenca)
        total_frase = total_frase + len(separa_frases(sentenca))
    total_palavra = 0
    lista_palavra = []
    
    for frase in lista_frase:
        lista_palavra = lista_palavra + separa_palavras(frase)
        total_palavra = total_palavra + len(separa_palavras(frase))
    wal2 = total_caracteres(lista_palavra) / total_palavra
    ttr2 = n_palavras_diferentes(lista_palavra) / total_palavra
    hlr2 = n_palavras_unicas(lista_palavra) / total_palavra
    sal2 = total_caracteres(lista_sentencas) / len(lista_sentencas)
    sac2 = total_frase / len(lista_sentencas)
    pal2 = total_caracteres(lista_frase) / total_frase
    return [wal2, ttr2, hlr2, sal2, sac2, pal2]

def avalia_textos(textos, ass_cp):
    for i in range(0, len(textos)):
        for j in range(0, len(textos)):
            if ass_cp[i] < ass_cp[j]:
                posicao = i
    return posicao

assinatura = le_assinatura()
print();
textos = le_textos()
grau_similaridade = []
for texto in textos:
    grau_similaridade.append(compara_assinatura(calcula_assinatura(texto), assinatura))

print("O autor do texto ", avalia_textos(textos, grau_similaridade)+1, " está infectado com COH-PIAH")
