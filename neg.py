a=[2,-4,3,6,7,-8,10,15,-18,20]
b=[]
c=[]
d=[]
for x in a:
	if(x<0):
		b.append(x)
	elif(x%2==0):
		c.append(x)
	else:
		d.append(x)
print(b)
print(sum(b))
print(c)
print(sum(c))
print(d)
print(sum(d))
	