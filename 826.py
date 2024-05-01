def check_Type_Of_Triangle(a,b,c): 
    if (a**2 == a**2 + b**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2): 
        return ("Right-angled Triangle") 
    elif (a**2 > c**2 + b**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2): 
        return ("Obtuse-angled Triangle") 
    else: 
        return ("Acute-angled Triangle")
