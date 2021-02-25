import random
    
def busqueda_binaria(valor):
    inicio = 0
    final = len(lista)-1
    while inicio <= final:
        
        puntero = (inicio+final)//2
        
        if valor == lista[puntero]:
            return puntero #ver que pasa si lo cambio por valor
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None      
    
def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda == None:
        return f"El numero {valor}, no se encuentra"
    else: 
        return f"El numero {valor}, se encuentra en la posicion {res_busqueda}" 
        """si hubiesemos usado directamente busqueda_binaria(valor), ubiese tenido que correr toda la funcion de nuevo, pero con res_busqueda solo presenta el valor que se le asigno"""



if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    valor = int(input('Que numero quieres encontrar? '))
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    print(buscar_valor(valor))
    print(lista)
