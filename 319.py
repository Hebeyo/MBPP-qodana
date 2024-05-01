def find_long_word(text):
  import re
  return (re.findall(r"\b\w{5}\b", text))
