#metodos de cadenas

cadena1 = "hola que tal"
cadena2 = "bueno chau"

#print(dir(cadena1)) #da una lista de metodos aplicables al tipo de dato

#resultado = cadena1.upper() #pasa a mayuscula.
#resultado = cadena1.lower() #pasa a minuscula
#resultado = cadena1.capitalize() #solo la primera letra a minuscula. primero combierte todo a minuscula
#resultado = cadena2.find("chau") # busca un valor dentro , y nos pasa la posicion en la cadena-  si no esta retorna -1
#resultado = cadena1.index("z")# igual pero nos retorna una excepcion 
#resultado = cadena1.isnumeric()# si es numero devuelve true sino false
#resultado = cadena1.isalpha()# si es alfanumerico devuelve true sino false ( no incluye espacios )
#resultado = cadena1.count("a")# devuelve cantidad de coincidencias 
#resultado = len(cadena1)#cuenta caracteres. es una funcion 
#resultado = cadena1.startswith("h") # verifica que la cadena empieza con el dato que le demos
#resultado = cadena1.endswith("l") # verifica que la cadena termine con el dato que le demos
#resultado = cadena1.replace("que tal", "como estas")# reemplaza con lo que le pasemos uque coincida en la cadena original, por lo que le pasemos como segundo argumento.
resultado = cadena1.split(" ") # separa en cadenas diferentes dentro de una lista, segun el valor que le pasemos. en este caso un espacio.


print(resultado)