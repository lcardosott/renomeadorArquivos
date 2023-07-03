import os
import pytesseract
import cv2
from PIL import Image 

#O programa funciona, porém demora muito por conta do mesmo escanear a pagina inteira
#Explorar pytesseract para escanear uma porcentagem da pagina tipo (100%/ 10%), assim pegaria o titulo e demoraria 1/10

def corta_imagem(imagem, left, top, right, bottom):
    croped_image = imagem.crop((left, top, right, bottom))
#    croped_image.show()
    croped_image.save('imagemcortada.png')


def seta_tamanho(imagem, left, top, right, bottom):
    width, height = imagem.size
    left = 10
    top = 120
    right = width-10
    bottom = top+85
    return left, top, right, bottom



path = "/home/lulutoratora/Documents/2semestre/F228/P2"
os.chdir(path)
left, right, bottom, top = 0, 0, 0, 0

for file in os.listdir(): #le cada arquivo
    imagem = Image.open(file)
    left, top, right, bottom =  seta_tamanho(imagem, left, top, right, bottom)
    corta_imagem(imagem, left, top, right, bottom)

    imagem = cv2.imread('/home/lulutoratora/Documents/2semestre/F228/P2/imagemcortada.png')
    texto = pytesseract.image_to_string(imagem)
    titulo = texto.split("\n\n")
    materia = titulo[0]
    os.rename(file,materia)
    os.remove("imagemcortada.png") 