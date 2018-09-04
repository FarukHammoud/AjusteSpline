#AjusteSpline v2.0 by Faruk Hammoud,2016  EESC/USP
# v1.0 released 05/05/2016 
import lib

imagem_fundo = loadImage("")
passos = lib.GE_PASSOS()


def setup():
    size(1280,720)
    global imagem_fundo
    imagem_fundo = loadImage("back.jpg")
    lib.Inicializa()
    
def draw():
    
    passos.Passo(imagem_fundo)