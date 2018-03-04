s="write about organization"
def vowel(s):
	v=('a','e','i','o','u')
	for x in s:
		if x in v:
			s=s.replace(x,"")
	print(s)
vowel(s)