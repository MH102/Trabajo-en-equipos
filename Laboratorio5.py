#NOMBRES:

#Reto 1
#Entradas: Cadena
#Salidas: Cantidad de cada caracter
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
def eliminarElementosIguales(lista):
    if(lista==[]):
        return []
    elif(seRepiteCaracter(lista[0],lista,1)==False):
        return [lista[0]] + eliminarElementosIguales(lista[1:])
    else:
        return eliminarElementosIguales(lista[1:])
def seRepiteCaracter(caracter,lista,indice):
    if(indice==len(lista)):
        return False
    elif(caracter==lista[indice]):
        return True
    else:
        return seRepiteCaracter(caracter,lista,indice+1)
#Reto 2
#Entradas: Lista
#Salidas: Lista de vocales
#Restricciones: Se debe dar una lista no vacia
def crearListaVocales(lista):
    if(type(lista)!=list):
        return "Debe indicar una lista"
    elif(lista==[]):
        return "Lista vacia"
    else:
        return crearListaVocalesAux(lista,0)
def crearListaVocalesAux(lista,indice):
    if(indice==len(lista)):
        return []
    elif(esVocal(lista[indice])==True):
        return [lista[indice]]+crearListaVocalesAux(lista,indice+1)
    else:
        return crearListaVocalesAux(lista,indice+1)
def esVocal(elemento):
    if(type(elemento)!=str):
        return False
    elemento=elemento.lower()
    if(elemento=="a" or elemento=="e" or elemento=="i" or elemento=="o" or elemento=="u"):
        return True
    else:
        return False
#Reto 3
#Entradas: Elemento 1, Elemento2, Lista
#Salidas: Lista con elementos sumados
#Pre/Post Condiciones: Se deben dar 2 elementos, si el elemento 1 esta en la lista se agrega el elemento 2 justo despues
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
#Reto 5
#Entradas: Lista
#Salidas: Profundidad de la lista
#Restricciones: Se debe dar una lista no vacia
def profundidadLista(lista):
    if(type(lista)!=list):
        return "Debe indicar una lista"
    elif(lista==[]):
        return "Lista vacia"
    else:
        return profundidadListaAux(lista,1)
def profundidadListaAux(lista,profundidad):
    if(lista==[]):
        return profundidad
    elif(type(lista[0])==list):
        return profundidadListaAux(lista[1:],profundidadListaAux(lista[0],profundidad+1)-seRepiteLista(lista[1:]))
    else:
        return profundidadListaAux(lista[1:],profundidad)
def seRepiteLista(lista):
    if(lista==[]):
       return 0
    elif(type(lista[0])==list):
        return 1
    else:
       return seRepiteLista(lista[1:])
#Reto 6
#Entradas: Lista A, Lista B
#Salidas: Lista producto cartesiano A x B
#Restricciones: Se deben de dar listas en A y en B
def productoCartesiano(A,B):
    if(type(A)!=list or type(B)!=list):
        return "Debe indicar listas"
    elif(A==[] or B==[]):
        return []
    else:
        return productoCartesianoAux(A,B,0)
def productoCartesianoAux(A,B,indice):
    if(A==[]):
        return []
    elif(indice==len(B)):
        return productoCartesianoAux(A[1:],B,0)
    else:
        return [[A[0]] + [B[indice]]] + productoCartesianoAux(A[0:],B,indice+1)
