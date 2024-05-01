def largest_triangle(a, b):
    if (a < 0 or b < 0):
        return -1
    area = (3 * 3 ** 0.5 * a ** 2) / (4 * b)
    return area
