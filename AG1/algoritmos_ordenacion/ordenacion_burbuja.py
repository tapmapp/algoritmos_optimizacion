# ordenacion burbuja
def bubbleSort(lista):

    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j] , lista[j+1] =  lista[j+1], lista[j]

    print(lista)

alist = [12, 34, 45, 23, 54, 23, 25]
bubbleSort(alist)