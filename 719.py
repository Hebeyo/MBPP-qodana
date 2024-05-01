def text_match(text):
    import re
    patterns = 'ab*?'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
