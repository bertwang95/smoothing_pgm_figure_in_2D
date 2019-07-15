import numpy as np
import matplotlib.pyplot as plt
import open_pgm as op

def increase_resolution (name,t):
    # t=int(input('the number of times to increase the width and height：'))
    data=op.read_pgm(name)
    [row, column] = data[1]
    array = data[0]
    image=array.reshape(row,column)

    new_image=np.zeros((row*t,column*t))
    # the nearest neighbour
    for i in range(0,row):
        for j in range (0,column):

            for m in range (i*t,i*t+t):
                for n in range (j*t,j*t+t):
                    new_image[m][n]=image[i][j]

    # the bilinear

    # plt.imshow(new_image)
    # plt.show()
    return (new_image)

# increase_resolution(name='E:\\360MoveData\\Users\\Bert\\Desktop\\dissertation\\test00496.pgm')
