def smallest_num(xs):
  small = xs[0]
  for i in range(1, len(xs)):
    if xs[i] < small:
      small = xs[i]
  return small
