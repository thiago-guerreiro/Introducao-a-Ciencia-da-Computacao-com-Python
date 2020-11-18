def maiusculas(frase):
    pos = 0
    string1 = ''
    while pos < len(frase):
        if ord(frase[pos]) >= 65 and ord(frase[pos]) <=90:
            string1 += frase[pos]
        pos += 1
    return string1
