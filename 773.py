def occurance_substring(text,pattern):
    s = text.find(pattern)
    return (text[s:s+len(pattern)], s, s+len(pattern))
