## 김결

def bubbleSort(a, n):
    for i in range(n, 0, -1):
        for j in range(1,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]