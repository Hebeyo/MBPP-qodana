def check_char(string):
	import re
	regex = r'^[a-z]$|^([a-z]).*\1$'
	if(re.search(regex, string)):
		return "Valid"
	else:
		return "Invalid"
