def most_common_elem(s,a):
  from collections import Counter
  most_common_elem=Counter(s).most_common(a)
  return most_common_elem
