def sort_list(test_list):
  test_list.sort(key = lambda i: len(str(i)))
  return (str(test_list))
