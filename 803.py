def is_Perfect_Square(n) :
    if (n >= 0):
        if (n == 0 or n == 1):
            return True
        i = 1
        while (i * i <= n):
            if ((n % i == 0) and (n / i == i)):
                return True     
            i = i + 1
    return False
