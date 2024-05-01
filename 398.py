def sum_of_digits(nums):
    result = 0
    for n in nums:
        if isinstance(n, int):
            result += sum(int(el) for el in str(n) if el.isdigit())
        elif isinstance(n, list):
            result += sum_of_digits(n)
    return result
