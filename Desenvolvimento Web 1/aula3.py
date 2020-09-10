#Distância Euclidiana
def quadrado_num(num):
    return num**2
    print (quadrado_num(2))

def raiz_quadrada(num):
    return num**(1/2)
    print (raiz_quadrada(9))

def dist_euclidiana (x1,x2,y1,y2):
    global euclidiana
    euclidiana = raiz_quadrada(quadrado_num(x2-x1)+quadrado_num(y2-y1))
    return euclidiana
    
distancia = dist_euclidiana(1,3,1,3)
print('A distancia dos dois pontos é {}'.format(distancia))
print (euclidiana)