sistema = [25, 10, 5 , 1]

def cambio_monedas(cantidad, sistema):
  
  solucion = [0 for i in range(len(sistema))]
  
  valorAcumulado = 0
  
  for i in range(len(sistema)):
    
    monedas = int((cantidad  - valorAcumulado) / sistema[i])
    solucion[i] = monedas
    
    valorAcumulado += monedas * sistema[i]
    
    if valorAcumulado == cantidad:
      return solucion
    
cambio_monedas(100, sistema)