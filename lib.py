pontos = []
curvas = []

def DesenhaSpline():
    strokeWeight(5)
    stroke(0,255,0)
    l_p = CalcularSpline()
    if Ponto.numero_de_pontos > 2:
        for i in range(len(l_p)):
            for x in range(pontos[i*2].x,pontos[i*2+2].x,1):
                point(x,l_p[i][0]*pow(x,3)+l_p[i][1]*pow(x,2)+l_p[i][2]*x+l_p[i][3])
    print("n pontos 2: "+str(len(pontos)))
    for ponto in pontos:
       strokeWeight(5)
       stroke(255,50-50*random(1),50-50*random(1))
       point(ponto.x,ponto.y)
       
       
def CalcularSpline():
    da = 0.1
    lista_parametros = []
    if Ponto.numero_de_pontos > 2:
        for i in range(0,Ponto.numero_de_pontos-2,2):
            
            lista = []
            
            x1 = pontos[i].x
            y1 = pontos[i].y
            x2 = pontos[i+1].x
            y2 = pontos[i+1].y
            x3 = pontos[i+2].x
            y3 = pontos[i+2].y
            
            print(x1,x2,x3,y1,y2,y3,da)
            
            Mo = [[pow(x1,3),pow(x2,3),pow(x3,3),3*pow(x1,2)],[pow(x1,2),pow(x2,2),pow(x3,2),2*x1],[x1,x2,x3,1],[1,1,1,0]]
            Ma = [[y1,y2,y3,da],[pow(x1,2),pow(x2,2),pow(x3,2),2*x1],[x1,x2,x3,1],[1,1,1,0]]
            Mb = [[pow(x1,3),pow(x2,3),pow(x3,3),3*pow(x1,2)],[y1,y2,y3,da],[x1,x2,x3,1],[1,1,1,0]]
            Mc = [[pow(x1,3),pow(x2,3),pow(x3,3),3*pow(x1,2)],[pow(x1,2),pow(x2,2),pow(x3,2),2*x1],[y1,y2,y3,da],[1,1,1,0]]
            Md = [[pow(x1,3),pow(x2,3),pow(x3,3),3*pow(x1,2)],[pow(x1,2),pow(x2,2),pow(x3,2),2*x1],[x1,x2,x3,1],[y1,y2,y3,da]]
            
            if Det(Mo) != 0:
                
                lista.append(Det(Ma)/Det(Mo))
                lista.append(Det(Mb)/Det(Mo))
                lista.append(Det(Mc)/Det(Mo))
                lista.append(Det(Md)/Det(Mo))
            
                lista_parametros.append(lista)
           
                da = lista[0]*3*pow(x3,2) + lista[1]*2*x3 + lista[2]
            
    return lista_parametros

original_millis = 0

def Det(l):
    n=len(l)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(Det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        if l[0][0]*l[1][1]-l[0][1]*l[1][0] == 0:
            return 1
        else:
            return (l[0][0]*l[1][1]-l[0][1]*l[1][0])

def Inicializa():
    background(30,200,40)
def Clear(imagem):
    image(imagem,0,0,width,height)    
class GE_PASSOS:
    
    def __init__(self,passo = 1):
        self.passo = passo
    def Passo(self,imagem_fundo):
        if self.passo == 1:
            Clear(imagem_fundo)
            self.Passo1()
        elif self.passo == 2:
            Clear(imagem_fundo)
            self.Passo2()
        elif self.Passo == 3:
            self.Passo3()
    def Passo1(self):
        global pontos
        fill(200-200*random(1)/8,200-200*random(1)/8,255)
        textSize(35)
        text("Passo 1: Clique nos pontos que voce deseja unir com uma spline",50,60)
        global mousePressed
        if Ponto.numero_de_pontos > 0 :
            noStroke()
            if mouseX > 1000 and mouseX < 1300 and mouseY > 600 and mouseY < 700 :
                if mousePressed :
                    self.passo = 2
                    print("n pontos: "+str(len(pontos)))
                fill(200,200,200,200)
            else:
                fill(200,200,200,50)
            rect(1000,600,300,100,20)
            textSize(60)
            fill(250,250,250,200)
            text("Concluir",1020,674)
        if mousePressed:
            global original_millis
            if millis() > original_millis + 500:
                global original_millis
                original_millis = millis()
                ponto = Ponto()
                ponto.MudaPonto([mouseX,mouseY])
                pontos.append(ponto)
           
                
        
        for ponto in pontos:
            strokeWeight(5)
            stroke(255,50-50*random(1),50-50*random(1))
            point(ponto.x,ponto.y)
        
    def Passo2(self):
        DesenhaSpline()
        self.passo = 3
    def Passo3(self):
        pass           
class Ponto:
    numero_de_pontos = 0
    def __init__(self,lista = [0,0]):
        self.x = lista[0]
        self.y = lista[1]
        Ponto.numero_de_pontos += 1
    def ListaPontos(self):
        lista = []
        lista.append(self.x)
        lista.append(self.y)
        return lista
    def MudaPonto(self,lista):
        if len(lista) == 2:
           self.x = lista[0]
           self.y = lista[1]