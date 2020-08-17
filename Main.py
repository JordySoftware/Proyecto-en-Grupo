from WordCloud import generateImage
from UsersTags import getTags

flag = True

while flag:
  print("\n Bienvenido al Request de stack OverFlow")
  userid = input("\n Digite el ID del usuario de quien desea generar sus etiquetas o si desea salir digite y: ")
  
  if userid == "y" or userid == "Y":
        flag = False
        print("Saliendo.................")
        break
  
  tags = getTags(userid)
  
if tags == None:
   print("Error al ingresar el id")
elif tags == "-1":
   print("No tiene tags el usuario")
else:
   generateImage(tags, "image/cloud.png")
