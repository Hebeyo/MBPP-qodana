def breakSum(n): 
	if (n == 0 or n == 1): 
		return n
	return max(n, breakSum(int(n/2)) + breakSum(int(n/3)) + breakSum(int(n/4)))
