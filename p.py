a=range(1,101)

print([x**3 if x%2  else x**2 for x in a if x%3])
