# ordenacion rapida
A = [9187, 244, 4054, 9222, 8373, 4993, 5265, 5470, 4519, 7182, 2035, 3506, 4337, 7580, 2554, 2824, 8357, 4447, 7379]

def quick_sort(A):
  if len(A) == 1:
    return A
  if len(A) == 2:
    return [min(A), max(A)]
  
  LEFT=[]
  RIGHT=[]
  
  pivote = (A[0]+ A[1] + A[2])/3
  
  for i in A:
    if i <= pivote :
      LEFT.append(i)
    else:
      RIGHT.append(i)
      
  return quick_sort(LEFT) + quick_sort(RIGHT)

quick_sort(A)
