def merge_dict(d1,d2):
 d = d1
 for key in d2:
  d[key] = d2[key]
 return d
