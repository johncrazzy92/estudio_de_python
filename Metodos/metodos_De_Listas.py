#metodos de lista

list = list(["hola","chau",5]) #crea una lista

#resultado = len(list) # len aqui funciona para saber el tamaño del array 
list.append("que ondas")#agrega un elemento a la lista
list.insert(1,"que pasa")#igual, pero como primer parametro se coloca el lugar del elemento que queremos insertar 
list.extend([False,"lol",12548])# se agrega una lista a otra lista 
list.pop(-1)#elimina un elemento de la lista segun el indice de parametro -  -1 elimina el ultimo 
list.remove("chau")#elimina segun el valor que pasemos 
#list.clear() #elimina todo

number = [128,1, 5 , 6 , 8 ,125 , 468]
number.sort(reverse=True)#ordena la lista - si tiene reverse true como parametro , ordeba al revez
number.reverse()#la revierte, pero sin ordenarla .

result = list.index("hola")

print(result)