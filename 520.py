def get_lcm(l):
  num1 = l[0]
  num2 = l[1]
  lcm = num1 if num1 > num2 else num2
  while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
      for i in range(2, len(l)):
        if lcm % l[i] != 0:
          lcm += 1
          break
      else:
        return lcm
    else:
      lcm += 1
