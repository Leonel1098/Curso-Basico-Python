print("Ingrese la contraseña")
contraseña = input()
print("Confirme la contraseña")
contra = input()
if(contraseña == contra.lower() ):
    print("Bienvenido al Sistema")
else: 
    print("Ingrese la contraseña de nuevo")

print("------------------------------------------------------------")
print("Ingrese su nombre")
name=input()
print("Ingrese su genero")
genero=input()

if genero == "M":
    if name.lower() < "m":
        grupo = "A"
    else: 
        grupo = "B"
else:
        if name.lower() >"n":
            grupo = "A"
        else:
            grupo = "B"
print("Su grupo asignado es " +grupo)
