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

    c=int(((n-1)/2))
    after_smooth=np.zeros([new_row-c,new_column-c])  #the array to contain the after smooth array

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
            # med = fd.find_median(filter_array)
            # med = int(med)
            # # print(med)
            # after_smooth[m][k] = med

            # use the find most frequency
            filter_list=filter_array.tolist()
            Z=fmf.find_most_frequency(filter_list)
            z=Z[1]
            if z>(n*n-1)/2:
                med=Z[0]
            else:
                med = fd.find_median(filter_array)
            med = int(med)
            # print(med)
            after_smooth[m][k] = med

            # # use the counter
            # filter_list = filter_array.tolist()
            # Max=Counter(filter_list).most_common(1)
            # z=Max[0][1]
            # if z > (n * n - 1) / 2:
            #     med = Max[0][0]
            # else:
            #     med = fd.find_median(filter_array)
            # med = int(med)
            # # print(med)
            # after_smooth[m][k] = med
    elapsed=(time.time()-start)
    print('time used',elapsed)
    # file = open('2Dcheck\\AfterimfCircleWithTriangle1.pgm', 'w')
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
