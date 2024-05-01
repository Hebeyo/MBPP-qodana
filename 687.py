def recur_gcd(a, b):
    if a == 0:
        return b
    return recur_gcd(b % a, a)
