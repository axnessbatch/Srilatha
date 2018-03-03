l=[1,2,3,4,2,2]
#v=[x for x,d in enumerate(l) if(d==2)]
#print(len(v))
s=[]
for x in l:
	if(x==2):
		s.append(x)
print(len(s))