
lista = [1, 5, -10, 20, 2, 3]
#Ordenar lista asendente
sorted(lista) 
#ordenar lista desendente
sorted(lista, reverse=True)

diccionario = {'a': 1, 'b': 5, 'c': 2}

#ordenar diccionario
sorted(diccionario.items(), key=lambda x: x[0]) #[('a', 1), ('b' ,5), ('c' ,2)]
sorted(diccionario.items(), key=lambda x: x[1]) #[('a', 1), ('c' ,2), ('b' ,5)]

#zip

nombres = ['natanael', 'juan', 'jonathan']
emails = ['n@gmail.com', 'j@gmail.com', 'jo@gmail.com']

for n, e in zip(nombres, emails)
	print 'Nombre: ', n, ', Email: ',e 

zip(nombres, emails);

dict(zip(nombres, emails))

#obtener solo los positico de una lista
lista = [5 ,0, -1, 6, 2, -9]
positivo = list()

#primera manera
for n in lista:
	if n > 0:
		positivo.append(n)
#segunda manera
positivo = []
positivo = [l for l in lista if l > 0]

#numero pares de un diccionario
pares = [{k:v} for k, v in diccionario.items() if v%2 == 0]

#set
lista1 = [1,2,3,4]
lista2 = [3,4,5,6]

#quitamos lo de la lista2 en la lista1
set(lista1) - set(lista2)

#quitamos lo de la lista 1 en la lista 2
set(lista2) - set(lista1)

#los valores que estan en anvas lista
set(lista1) & set(lista2)

#unimos anvas lista 
set(lista1) | set(lista2)

#limpiar la lista de los valores repetidos
lista = [1,2,3,4,1,2,5]
set(lista)
lista = list(set(lista))















