# lista
# array igual que en js
lista = ["hola", "adios", "hasta mañana", True, 158]
#tuplas no puede modificarse , se escriben con ()
tupla = ("hola", "adios", "hasta mañana", True, 158)
#print como log en js y se puede usar el indice de un array con []
lista[0] = "bebe" #modifica el array
#tupla[0] = "bebe" #no lo modifica pero se puede redefinir
print(lista[0])

#creando un set ( conjunto )

conjunto = {"hola", "adios", "hasta mañana", True, 158, "adios"} #no puede haber elementos duplicados
#se puede redefinir  
conjunto = {"redefinido"}
#conjunto[0] = {"hola"}  ---------- pero no modificar
#print(conjunto[0])  no puedo acceder por el indice en un set

#diccionario ( dict ) se accede al dato desde la key
diccionario = {
    'nombre': 'john',
    'apellido': 'romero',
    'edad': 31
}
print(diccionario['nombre'] + ' es mi nombre')
