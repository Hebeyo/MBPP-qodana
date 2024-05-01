def common_prefix(arr, n):
  prefix = arr[0]
  for i in range(1, n):
    j = 0
    while j < len(prefix) and j < len(arr[i]) and prefix[j] == arr[i][j]:
      j += 1
    prefix = prefix[:j]
  return prefix
