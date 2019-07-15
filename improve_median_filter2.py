import numpy as np
import find_median as fd
import border as bo
import open_pgm as op
import matplotlib.pyplot as plt
from collections import Counter
import time
import find_most_frequency as fmf

def two_d_improve_median_filter(name):
    t=int(input('the number of times to increase the width and height：'))
    n=int(input('the size of filter:'))
    k=int((n-1)/2)

    # A=[9,1,2,3,4,5,6,7,8,5,6,7]
    # array_A=np.array(A)
    # image=array_A.reshape(4,3)
    # print(image)
    data=op.read_pgm(name)
    [row,column]=data[1]
    list=data[0]
    array=np.array(list)
    image=array.reshape(row,column)
    # plt.imshow(image)
    # plt.show()


    new_image=bo.border(name,n,t)

    # plt.imshow(new_image)
    # plt.show()

    # [row,column]=image.shape  #get the original image shape
    [new_row, new_column]=new_image.shape   #get the newimage shape

    c = int(((n - 1) / 2))
    after_smooth=np.zeros([new_row,new_column])  #the array to contain the after smooth array

    filter_array=np.zeros([n*n])
    # print(filter_array)

    start=time.time()
    d = {x: 0 for x in range(0, 4)}
    d[0]=n*n
    for j in range (int((n-1)/2),new_row-n+1):
        for k in range(1, new_column - n):
            for m in range (0,n):
                d[new_image[j + c][k - 1]] -=1
                d[new_image[j - c][k - 1]] -= 1
                d[new_image[j][k - 1]] -= 1
                d[new_image[j + c][k + n - 1]] +=1
                d[new_image[j - c][k + n - 1]] += 1
                d[new_image[j][k + n - 1]] += 1
                # for x in range(0, n):
                #     if x == new_image[j + int((n-1)/2)][k - 1]:
                #         d[x] -= 1
                #     if x == new_image[j - int((n-1)/2)][k - 1]:
                #         d[x] -= 1
                #     if x == new_image[j ][k - 1]:
                #         d[x] -= 1
                #     if x == new_image[j ][k + n - 1]:
                #         d[x] += 1
                #     if x == new_image[j + int((n-1)/2)][k + n - 1]:
                #         d[x] += 1
                #     if x == new_image[j - int((n-1)/2)][k + n - 1]:
                #         d[x] += 1
            sum = 0
            for i in range(0, 3):
                if sum + d[i] > (n * n) / 2:
                    med = i
                else:
                    sum = d[i]

            med = int(med)
            # print(med)
            after_smooth[j][k] = med


    elapsed=(time.time()-start)
    print('time used',elapsed)
    # file = open('2Dcheck\\Afterimf2CircleWithTriangle.pgm', 'w')
    # [m, n] = after_smooth.shape
    # max = 2
    # file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
    # for i in range(0, m):
    #     for j in range(0, n):
    #         file.write(str(int(after_smooth[i][j])) + '\n')
    # file.close()

    plt.imshow(after_smooth)
    plt.show()
    return (after_smooth)

two_d_improve_median_filter(name='2Dcheck\\OriginalPerfectCircleWithTriangle.pgm')
