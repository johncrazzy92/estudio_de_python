edad = 18

#muy similar a if() else() pero sin parentesis y con :

if edad >= 18:
    print("Eres mayor")
else:
    print("Eres menor")
    
contraseña = ""

if contraseña == "imcreep92":
    print("contraseña aceptada")
elif contraseña == "": # else if  se escribe como "elif"
    print("necesitas colocar una contraseña")
else:
    print("contraseña erronea")