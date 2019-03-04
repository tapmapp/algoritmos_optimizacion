import random
import math

N=100

LISTA_2D = [  (random.randrange(1,N*10),random.randrange(1,N*10) )  for _ in range(N)]

def distancia_divide_y_venceras(L):
  #Si hay pocos por Fuerza Bruta
  if len(L) <10: 
    return  distancia_fuerza_bruta(L)
  
  
  #Dividir en listas grandes
  #pivite =  sum([L[i][0]for i in range(len(L))]) / len(L)
  
  
  LISTA_IZQ = sorted(L, key=lambda x: x[0])[:len(L)//2]
  LISTA_DER = sorted(L, key=lambda x: x[0])[len(L)//2:]
  
  PUNTOS_LISTA_IZQ = distancia_divide_y_venceras(LISTA_IZQ)
  PUNTOS_LISTA_DER = distancia_divide_y_venceras(LISTA_DER)
  
  return distancia_fuerza_bruta(PUNTOS_LISTA_IZQ + PUNTOS_LISTA_DER)
  

@calcular_tiempo  
def LANZA(L):
  return distancia_divide_y_venceras(L)
  
SOL = LANZA(LISTA_2D[:1000])

print(SOL)