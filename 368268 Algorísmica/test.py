def suma(a: int, b: int) -> int:
	return a + b

def resta(a: int, b:int) -> int:
	return a - b

def sumres(a:int, b:int) -> int:
	s:int = suma(a, b)
	d:int = resta(a, b)
	return s, d

a:int = 5
b:int = 3

result = sumres(a, b)
print (result)




