import numpy as np
import find_most_frequency as fmf
import border as bo
import open_pgm as op
import matplotlib.pyplot as plt
import time
from collections import Counter

def two_d_improve_most_frequency_filter(name):
    t=int(input('the number of times to increase the width and height：'))
    n=int(input('the size of filter:'))
    k=int((n-1)/2)
    # head='E:\\360MoveData\\Users\\Bert\\Desktop\\dissertation\\'

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
    after_smooth = np.zeros([new_row - c, new_column - c])  # the array to contain the after smooth array

    filter_array=np.zeros([n*n])
    # print(filter_array)

    start=time.time()
    for m in range (new_row-n):
        for k in range (new_column-n):
            q=0
            filter_array = np.zeros([n * n])
            for i in range(m,m+n):
                for j in range (k,k+n):
                    filter_array[q] = int(new_image[i][j])
                    q += 1

            # # normal
            # filter_list=filter_array.tolist()
            # M=fmf.find_most_frequency(filter_list)
            # max=M[0]
            # max=int(max)
            # after_smooth[m][k]=max

            # use the counter
            filter_list = filter_array.tolist()
            Max=Counter(filter_list).most_common(1)
            z=Max[0][1]
            if z>(n*n-1)/2:
                max=Max[0][0]
            else:
                M = fmf.find_most_frequency(filter_list)
                max=M[0]
            # print(max)
            max=int(max)
            after_smooth[m][k] = max

    elapsed = (time.time() - start)
    print('time used', elapsed)
    # print(after_smooth)
    file = open('2Dcheck\\AfterimffCircleWithTriangle.pgm', 'w')
    [m, n] = after_smooth.shape
    max = 2
    file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
    for i in range(0, m):
        for j in range(0, n):
            file.write(str(int(after_smooth[i][j])) + '\n')
    file.close()

    plt.imshow(after_smooth)
    plt.show()
    return (after_smooth)

two_d_improve_most_frequency_filter(name='2Dcheck\\OriginalPerfectCircleWithTriangle.pgm')