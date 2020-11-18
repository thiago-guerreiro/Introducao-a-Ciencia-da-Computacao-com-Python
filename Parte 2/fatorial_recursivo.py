def fatorial(n: int) -> int:
    return 1 if n < 1 else n * fatorial(n-1)
