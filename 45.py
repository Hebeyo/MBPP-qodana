def get_gcd(l):
  num1 = l[0]
  num2 = l[1]
  gcd = num1
  for i in range(2, len(l)):
    num2 = l[i]
    while(num2):
      num1, num2 = num2, num1 % num2
    gcd = num1
  return gcd
