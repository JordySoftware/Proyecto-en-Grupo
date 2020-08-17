
#Importar Carpetas
!git clone https://github.com/JordySoftware/Proyecto-en-Grupo.git

#*********************************** USERS TAGS **************************************
import requests
import json

def getTags(user_id):
    url = f"https://api.stackexchange.com/2.2/users/{user_id}/top-tags?site=es.stackoverflow"

    r = requests.get(url)
    r_json = r.json()

    tags = ""

    if "error_id" in r_json: 
      return None
    elif not r_json["items"]:
        return "-1"
    else:
        for tag in r_json["items"]:
          tags += tag["tag_name"] + " "
        tags = tags.replace("-", "")
        return tags
#*********************************** WORD CLOUD **************************************
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def generateImage(words, custom_mask):
    c_mask = np.array(Image.open(custom_mask)) #Tomamos la imagen de la nube
    wc = WordCloud(background_color="white", mask=c_mask, regexp= r"\S[\S']+") #Personalizamos la nube
    wc.generate(words)# Genera las palabras
    plt.imshow(wc,interpolation="bilinear") #Genera la nube con las palabras
    plt.axis("off") #Muesrtra una cuadricula
    plt.show() #Presenta una ventana emergente con la nube


#*********************************** MAIN **************************************
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
      generateImage(tags, "/content/Proyecto-en-Grupo/image/cloud.png")



