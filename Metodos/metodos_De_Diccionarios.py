#metodos de diccionarios

dic = {
    "nombre" : 'juan',
    "apellido" : 'romero',
    "edad" : 31
} 

metodo4 = dic.pop("apellido")#elimina un elemento o mas del diccionario ( nos lo devuelve )
metodo = dic.keys()#devuelve un objeto dic_item
metodo2 = dic.get("nombre")#get nos devuelve el valor de la clave que le demos, sin embargo a diferencia de ponerlo como dic[clave], 
                           #hacerlo con get, no nos frena el programa con una excepcion, sino que nos devuelve none ( undefined de js )
#metodo3 = dic.clear() ----- limpia el diccionario
metodo5 = dic.items()#itera el diccionario en todos sus elementos

print(metodo5)