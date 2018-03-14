#Reto 1
#Entradas: Cadena
#Salidas: Cantidad de cada Caracter
#Restricciones: Se debe dar una cadena, la cadena no puede ser vacia
def contarCaracteres(cadena):
    if(type(cadena)!=str):
        return "Debe indicar una cadena"
    elif(cadena==""):
        return "Cadena no valida"
    else:
        return eliminarElementosIguales(contarCaracteresAux(cadena,0))
def contarCaracteresAux(cadena,x):
    if(x==len(cadena)):
       return []
    else:
       return [compararCaracteres(cadena[x],cadena,len(cadena)-1,0)] + contarCaracteresAux(cadena,x+1)
def compararCaracteres(caracter,cadena,contador,cantidad):
       if(contador==-1):
           return [caracter,cantidad]
       elif(caracter==cadena[contador]):
           return compararCaracteres(caracter,cadena,contador-1,cantidad+1)
       else:
           return compararCaracteres(caracter,cadena,contador-1,cantidad)
def eliminarElementosIguales(cadena):
    if(cadena==[]):
        return []
    elif(seRepite(cadena[0],cadena,1)==False):
        return [cadena[0]] + eliminarElementosIguales(cadena[1:])
    else:
        return eliminarElementosIguales(cadena[1:])
def seRepite(caracter,cadena,indice):
    if(indice==len(cadena)):
        return False
    elif(caracter==cadena[indice]):
        return True
    else:
        return seRepite(caracter,cadena,indice+1)
#Reto 2
#Entradas:
#Salidas:
#Restricciones:
    
#Reto 3
#Entradas: Elemento 1, Elemento2, Lista
#Salidas: Lista con elementos sumados
#Pre/Post Condiciones:????
#Restricciones: Se debe ingresar una lista
def insertarElemento(elemento1,elemento2,lista):
    if(type(lista)!=list):
        return "Indicar una lista"
    elif(lista==[]):
        return []
    else:
        return insertarElementoAux(elemento1,elemento2,lista)
def insertarElementoAux(elemento1,elemento2,lista):
    if(lista==[]):
        return []
    elif(lista[0]==elemento1):
        return [lista[0]]+[elemento2]+insertarElementoAux(elemento1,elemento2,lista[1:])
    else:
        return [lista[0]]+insertarElementoAux(elemento1,elemento2,lista[1:])
#Reto 4
#Entradas: Lista
#Salidas: Los primeros elementos en cada lista
#Restricciones: Se debe dar una lista no vacia
def obtenerPrimeros(lista):
    if(type(lista)!=list):
        return "Debe indicar una lista"
    elif(lista==[]):
        return "Lista vacia"
    else:
        return obtenerPrimerosAux(lista)
def obtenerPrimerosAux(lista):
    if(lista==[]):
        return []
    else:
        return extraerElemento(lista[0])+obtenerPrimerosAux(lista[1:])
def extraerElemento(lista):
    return [lista[0]]
