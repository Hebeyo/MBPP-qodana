def find_char(text):
  import re
  return (re.findall(r"\b\w{3,5}\b", text))
