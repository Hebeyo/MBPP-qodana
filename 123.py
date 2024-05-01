def amicable_numbers_sum(n):
    def d(n):
        return sum([i for i in range(1, n) if n % i == 0])
    amicable = set()
    for i in range(2, n+1):
        a = d(i)
        if a != i and d(a) == i:
            amicable.add(i)
            amicable.add(a)
    return sum(amicable)
