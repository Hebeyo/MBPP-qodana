def check_date(m, d, y):
    try:
        m, d, y = map(int, (m, d, y))
        if m<1 or m>12:
            return False
        if d<1 or d>31:
            return False
        if y<1 or y>9999:
            return False
        return True
    except ValueError:
        return False
