def basesnum_coresspondingnum(bases_num,index):
  result = list(map(lambda x, y: x ** y, bases_num, index))
  return result
