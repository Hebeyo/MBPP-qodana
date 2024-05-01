def extract_quotation(text1):
  import re
  return (re.findall(r'"(.*?)"', text1))
