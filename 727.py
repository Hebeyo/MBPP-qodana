def remove_char(S):
  import re 
  result = re.sub('[\W_]+', '', S) 
  return result
