def extract_max(input):
  import re
  numbers = re.findall('\d+',input)
  numbers = map(int,numbers)
  return max(numbers)
