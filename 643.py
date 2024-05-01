def text_match_wordz_middle(text):
    import re
    patterns = '\Bz\B'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
