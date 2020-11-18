def menor_nome(lista):
    i = 1
    menor = lista[0].strip()
    while i < len(lista):
        if len(menor) > len(lista[i].strip()):
            menor = lista[i].strip()
        i += 1
    return menor.lower().capitalize()
