import numpy as np
from collections import deque

def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp

def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = L_length // 2
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]

def find_median(array):
    L=deque(array)
    L.appendleft(0)
    A=heap_sort(L)
    k=int(len(array))
    i=int((k-1)/2)
    med=int(A[i])




    return (med)

# improve_find_median(array=[1,2,2,2,3,3,3,5,2,3],max=5)