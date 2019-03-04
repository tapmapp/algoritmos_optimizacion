import random
import math

N=100

LISTA_2D = [  (random.randrange(1,N*10),random.randrange(1,N*10) )  for _ in range(N)]

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

distancia_fuerza_bruta(LISTA_2D)