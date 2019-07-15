import operator
import find_median as fm

def find_most_frequency(L):
    d={}

    for i in L:
        if i not in d.keys():
            d[i]=L.count(i)
    A=sorted(d.items(),key=operator.itemgetter(1),reverse=True)

    if len(A)==1:
        max=A[0][0]
        fre=A[0][1]
    elif A[0][1]==A[1][1]:
        max=fm.find_median(L)
        fre=A[0][1]
    else:
        max=A[0][0]
        fre=A[0][1]

    # print(d.items())
    # print(A)
    # print(len(A))
    # print(A[0])
    # print(A[0][1])
    # print(max)
    return (max,fre)

# find_most_frequency (L=[2,2,2,2])
