def remove_extra_char(text1):
  import re
  pattern = re.compile('[\W_]+')
  return (pattern.sub('', text1))
