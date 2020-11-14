def ehPrimo(k):
    dvs = 0
    for div in range(1, k):
        if k % div == 0:
            dvs = dvs + 1
        if dvs > 1:
          break
    if dvs > 1:
        return False
    else:
        return True

def maior_primo(x):
    primo = x
    i = 0
    while i <= x:
        if ehPrimo(i):
            primo = i
        i = i + 1
    return primo
