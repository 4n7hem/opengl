#Declare as cores de cada unidade de cubo (eu vou precisar declarar isso 27 vezes.)

#A ordem das cores é: frente, tras, encima, embaixo, direita, esquerda.
#As cores são:  
vermelho = [1, 0, 0]
verde=[0, 1, 0]
azul = [0, 0, 1]
branco = [1, 1, 1]
laranja = [1, 0.6, 0]
amarelo =[1, 1, 0]
preto = [0,0,0] #(para lados que não são válidos, ou seja, estão na parte de dentro do cubo)

#Serão declaradas as cores na ordem de: linhas, colunas, altura, sendo o cubo mais a esquerda, atrás e superior é o cubo [0,0,0]
def cuboSolucionavel():
    #placeholder cores.append([preto,preto,preto,preto,preto,preto]) #cubo [0,0,0]
    cores=[]
    cores.append([preto,amarelo,preto,verde,preto,laranja]) #cubo [0,0,0]
    cores.append([preto,amarelo,preto,preto,preto,verde]) #cubo [0,1,0]
    cores.append([preto,amarelo,azul,preto,preto,laranja]) #cubo [0,2,0]
    cores.append([preto,vermelho,preto,amarelo,preto,preto]) #cubo [1,0,0]
    cores.append([preto,laranja,preto,preto,preto,preto]) #cubo [1,1,0]
    cores.append([preto,verde,branco,preto,preto,preto]) #cubo [1,2,0]
    cores.append([preto,verde,preto,branco,vermelho,preto]) #cubo [2,0,0]
    cores.append([preto,laranja,preto,preto,verde,preto]) #cubo [2,1,0]
    cores.append([preto,verde,branco,preto,laranja,preto]) #cubo [2,2,0]
    #================================================================
    cores.append([preto,preto,preto,laranja,preto,azul]) #cubo [0,0,1]
    cores.append([preto,preto,preto,preto,preto,verde]) #cubo [0,1,1]
    cores.append([preto,preto,vermelho,preto,preto,azul]) #cubo [0,2,1]
    cores.append([preto,preto,preto,amarelo,preto,preto]) #cubo [1,0,1]
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [1,1,1] esse fica só tudo preto mesmo
    cores.append([preto,preto,branco,preto,preto,preto]) #cubo [1,2,1]
    cores.append([preto,preto,preto,branco,azul,preto]) #cubo [2,0,1]
    cores.append([preto,preto,preto,preto,azul,preto]) #cubo [2,1,1]
    cores.append([preto,preto,branco,preto,laranja,preto]) #cubo [2,2,1]
    #================================================================
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [0,0,2]
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [0,1,2]
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [0,2,2]
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [1,0,2]
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [1,1,2] 
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [1,2,2]
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [2,0,2]
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [2,1,2]
    cores.append([preto,preto,preto,preto,preto,preto]) #cubo [2,2,2]
    return cores