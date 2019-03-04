TARIFAS = [
[0,5,4,3,999,999,999],
[999,0,999,2,3,999,11],
[999,999, 0,1,999,4,10],
[999,999,999, 0,5,6,9],
[999,999, 999,999,0,999,4],
[999,999, 999,999,999,0,3],
[999,999,999,999,999,999,0]
]

#Paseo por el rio
def Precios(TARIFAS):
  N = len(TARIFAS[0])
  
  PRECIOS = [ [9999]*N for i in [9999]*N ]
  RUTAS    = [ [""]*N for i in [9999]*N ]
  

  
  for i in range(N-1):
    for j in range(i+1,N):
      MIN = TARIFAS[i][j]
      RUTAS[i][j] = i
      
      for k in range(i,j):
        if PRECIOS[i][k]+ TARIFAS[k][j] < MIN:
          MIN = min( MIN , PRECIOS[i][k]+ TARIFAS[k][j] )
          RUTAS[i][j] = k
      PRECIOS[i][j] = MIN
      
  return PRECIOS, RUTAS

  
PRECIOS, RUTAS = Precios(TARIFAS)

print(PRECIOS)

print()

print(RUTAS)

def calcular_ruta(RUTAS, desde, hasta):
  if desde == hasta:
    #print("Ir a :" + str(desde))
    return desde 
  else:
    return str(calcular_ruta(RUTAS, desde, RUTAS[desde][hasta])) +  ',' + str(RUTAS[desde][hasta]) 

print("\nLa ruta es:")  
calcular_ruta(RUTAS, 0,6)