# funció que retorna multiplicació de tres nombres enters
def mult(a:int, b:int, c:int) -> int:
	return a * b * c

print (mult(1, 2, 3))

# funció que mostra per pantalla 5 vegades "hola" i retornar "molt de gust"
def funcio2 (a:str) -> str:
	print (a * 5)
	return "molt de gust"

print(funcio2("hola"))

# funció que compta les "a" contingudes en una paraula
def comptar(a:str) -> int:
	return a.count("a")

print(comptar("hola"))


print("'manel'")
