#reinas
N = 4
solucion = [0 for i in range(N)]
etapa = 0

def es_prometedora(solucion, etapa):
  
  for i in range(etapa + 1):
    if solucion.count(solucion[i]) > 1:
      return False
    
    # verificar diagonales
    for j in range(i + 1, etapa + 1):
      if abs(i - j) == abs(solucion[i] - solucion[j]):
        return False
      
  return True

def escribe(solucion):
  n = len(solucion)
  for x in range(n):
    print("")
    for i in range(n):
      if solucion[i] == x + 1:
        print(" X ", end = "")
      else:
        print(" - ", end = "")

def reinas(N, solucion, etapa):
  
  for i in range(1, N+1):
    solucion[etapa] = i
  
    if es_prometedora(solucion, etapa):
      if etapa == N-1:
        # ultima etapa, imprimimos solucion
        print("\n\nLa solución es:")
        print(solucion)
        escribe(solucion)
      else:
        # no es prometedora
        reinas(N, solucion, etapa + 1)
    else:
      # no es prometedora
      None
    solucion[etapa] = 0
    
reinas(N, solucion, etapa)