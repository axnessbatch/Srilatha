a=[1,2,3,2,3,4,1,3,4]
b=[]
for x in a:
	if x not in b:
		b.append(x)
print(b)
print(sum(b))
d=len(b)
print((sum(b))/d)
	