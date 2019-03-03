# algoritmo de ordenacion
def insertionSort(alist):
    for i in range(1, len(alist)):

        value = alist[i]
        index = i

        while index > 0 and alist[index - 1] > value:
            alist[index] = alist[index - 1]
            index = index - 1

        alist[index] = value

alist = [12, 34, 45, 23, 54, 23, 25]
insertionSort(alist)
print(alist)