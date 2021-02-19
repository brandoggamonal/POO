def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper()

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido)

#@funcion_decoradora #esta es otra opcion para remplazar la opcion de arriba
#def zumbido():
#	print("Buzzzzzz")
