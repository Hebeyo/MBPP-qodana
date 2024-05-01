def search_literal(pattern,text):
    s = text.find(pattern)
    e = s + len(pattern)
    return (s, e)
