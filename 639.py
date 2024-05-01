def sample_nam(sample_names):
  result = []
  for i in sample_names:
    if i[0].isupper() and i[1:].islower():
      result.append(i)
  return len(''.join(result))
