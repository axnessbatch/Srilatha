n=int(input("enter a number"))
m=n
rev=0
while(n>0):
	r=n%10
	rev=rev*10+r
	n=n//10
print(rev)
if(m==rev):
	print("palindrome")
else:
	print("not palindrome")