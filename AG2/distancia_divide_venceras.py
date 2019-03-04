import random
import math

N=100

LISTA_2D = [  (random.randrange(1,N*10),random.randrange(1,N*10) )  for _ in range(N)]

def distancia_divide_y_venceras(L):
  #Si hay pocos por Fuerza Bruta
  if len(L) <10: 
    return  distancia_fuerza_bruta(L)
  
  LISTA_IZQ = sorted(L, key=lambda x: x[0])[:len(L)//2]
  LISTA_DER = sorted(L, key=lambda x: x[0])[len(L)//2:]
  
  PUNTOS_LISTA_IZQ = distancia_divide_y_venceras(LISTA_IZQ)
  PUNTOS_LISTA_DER = distancia_divide_y_venceras(LISTA_DER)
  
  return distancia_fuerza_bruta(PUNTOS_LISTA_IZQ + PUNTOS_LISTA_DER)
  
#Fuerza Bruta
def distancia_fuerza_bruta(L):
  mejor_distancia = 100000e10
  
  A,B = (),()
  
  for i in range(len(L)):
    for j in range(i+1, len(L)):
      D = distancia(L[i],L[j])
      if D < mejor_distancia:
        A,B=L[i],L[j]
        mejor_distancia = D
  return [A,B] 

SOL = distancia_divide_y_venceras(LISTA_2D[:1000])

print(SOL)