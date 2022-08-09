import csv
import os
import numpy as np
import matplotlib.pyplot as plt

print("------------------------------------------------------------------\nIgor Costa Pinheiro - DRE: 119047743\nTratamento de dados do projeto de elementos finitos\nDados baseados na simulação feita com MACH = 0,3\nARQUIVOS CSV DEVEM ESTAR NO MESMO DIRETÓRIO/PASTA DO CÓDIGO\n------------------------------------------------------------------")

def grafico_velocidadeu():
  u=[]
  x1=[]
  z=0
  for file in os.listdir():
    if file.endswith(".csv"):
      with open(file, "r") as arquivo:
        arquivo_csv= csv.reader(arquivo, delimiter=",")     
        for i, linha in enumerate(arquivo_csv):
          if i==0:
            continue
          else:
            for linhas in arquivo_csv:
              if linhas[1] =='1.#QNANe+0000' or linhas[1]=='1.#QNANe+000':
                linhas[1] = '0'
                u.append(float(linhas[1]))
                x1.append(float(linhas[9]))
              else:
                u.append(float(linhas[1]))
                x1.append(float(linhas[9]))
      arquivo.close()      
      plt.title('Perfil da velocidade em x')
      plt.xlabel('x')
      plt.ylabel('u')
      plt.plot(x1,u)
      u=[]
      x1=[]


  
  plt.show()


def grafico_velocidadev():
  for file in os.listdir():
    if file.endswith(".csv"):
      with open(file, "r") as arquivo:
        arquivo_csv= csv.reader(arquivo, delimiter=",")
        v=[]
        x2=[]
        for i, linha in enumerate(arquivo_csv):
          if i==0:
            continue
          else:
            for linhas in arquivo_csv:
              if linhas[2] =='1.#QNANe+0000' or linhas[1]=='1.#QNANe+000':
                linhas[2] = '0'
                v.append(float(linhas[2]))
                x2.append(float(linhas[9]))
              else:
                  v.append(float(linhas[2]))  
                  x2.append(float(linhas[9]))
      arquivo.close()
      plt.title('Perfil da velocidade em y')
      plt.xlabel('y')
      plt.ylabel('v')
      plt.plot(x2,v)
      v=[]
      x2=[]
      
  plt.show()

  
def grafico_velocidadew():
  for file in os.listdir():
    if file.endswith(".csv"):
      with open(file, "r") as arquivo:
        arquivo_csv= csv.reader(arquivo, delimiter=",")
        w=[]
        x3=[]
        
        for i, linha in enumerate(arquivo_csv):
          if i==0:
            continue
          else:
            for linhas in arquivo_csv:
              if linhas[3] =='1.#QNANe+0000' or linhas[1]=='1.#QNANe+000':
                linhas[3] = '0'
                w.append(float(linhas[3]))
                x3.append(float(linhas[9]))
              else:
                w.append(float(linhas[3]))
                x3.append(float(linhas[9]))
              
      arquivo.close()       
      plt.title('Perfil da velocidade em Z')
      plt.xlabel('z')
      plt.ylabel('w')
      plt.plot(x3,w)
      w=[]
      x3=[]
      
  plt.show()  

  
def grafico_pressaox():
  for file in os.listdir():
    if file.endswith(".csv"):
      with open(file, "r") as arquivo:
        arquivo_csv= csv.reader(arquivo, delimiter=",")
        x1=[]
        p=[]
        for i, linha in enumerate(arquivo_csv):
          if i==0:
            continue
          else:
            for linhas in arquivo_csv:
              if linhas[0] =='1.#QNANe+0000' or linhas[1]=='1.#QNANe+000':
                linhas[0] = '0'
                p.append(float(linhas[0]))
                x1.append(float(linhas[9]))
              else:
                p.append(float(linhas[0]))  
                x1.append(float(linhas[9]))
      arquivo.close()        
      plt.title('Perfil da pressão em x')
      plt.xlabel('x')
      plt.ylabel('p')
      plt.plot(x1,p)
      x1=[]
      p =[]

  plt.show()
      

def grafico_pressaoy():
  for file in os.listdir():
    if file.endswith(".csv"):
      with open(file, "r") as arquivo:
        arquivo_csv= csv.reader(arquivo, delimiter=",")
        x2=[]
        p=[]

        
        for i, linha in enumerate(arquivo_csv):
          if i==0:
            continue
          else:
            for linhas in arquivo_csv:
              if linhas[0] =='1.#QNANe+0000' or linhas[1]=='1.#QNANe+000':
                linhas[0] = '0'
                p.append(float(linhas[0]))
                x2.append(float(linhas[10]))
              else:
                p.append(float(linhas[0]))            
                x2.append(float(linhas[10]))
      arquivo.close()      
      plt.title('Perfil da pressão em y')
      plt.xlabel('x')
      plt.ylabel('p')
      plt.plot(x2,p)
      x2=[]
      p =[]
  plt.show()      

def grafico_pressaoz():
  for file in os.listdir():
    if file.endswith(".csv"):
      with open(file, "r") as arquivo:
        arquivo_csv= csv.reader(arquivo, delimiter=",")
        x3=[]
        p=[]

        
        for i, linha in enumerate(arquivo_csv):
          if i==0:
            continue
          else:
            for linhas in arquivo_csv:
              if linhas[0] =='1.#QNANe+0000' or linhas[1]=='1.#QNANe+000':
                linhas[0] = '0'
                p.append(float(linhas[0]))
                x3.append(float(linhas[11]))
              else:
                p.append(float(linhas[0]))  
                x3.append(float(linhas[11]))
      arquivo.close()        
      plt.title('Perfil da pressão em z')
      plt.xlabel('x')
      plt.ylabel('p')
      plt.plot(x3,p)
      x3=[]
      p =[]
  plt.show()      

while True:
  try:
    grafico=int(input('\nDigite:\n(1)- Para gráfico de velocidade u em x\n(2)- Para gráfico de velocidade v em y\n(3)- Para gráfico de velocidade w em z\n(4)- Para gráfico de pressão em x\n(5)- Para gráfico de pressão em y\n(6)- Para gráfico de pressão em z\n(0)- Para fechar o programa\n:'))
    if grafico == 1:
      grafico_velocidadeu()
    elif grafico == 2:
      grafico_velocidadev()
    elif grafico == 3:
      grafico_velocidadew()
    elif grafico == 4:
      grafico_pressaox()
    elif grafico == 5:
      grafico_pressaoy()
    elif grafico == 6:
      grafico_pressaoz()
    elif grafico == 0:
      break
  except:
    print('Caractere invalido, tente novamente')
print('\nFinalizado')
