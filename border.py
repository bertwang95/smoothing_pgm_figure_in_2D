import numpy as np
import open_pgm as op
import increase_resolution as ir
import matplotlib.pyplot as plt


def border(name,n,t):
    # t = int(input('the number of times to increase the width and height：'))
    image=ir.increase_resolution(name,t)
    # print(image)
    # data=op.read_pgm(name)
    # [row,column]=data[1]
    # array=data[0]
    # # print(array)
    # # print(row)
    #
    # # A=[9,1,2,3,4,5,6,7,8]
    # # array=np.array(A)
    # # image=array.reshape(3,3)
    # # row=3
    # # column=3
    # # print(image)
    # # array=np.array(name)
    # # row=4
    # # column=3

    [row,column]=image.shape
    # print(row,column)
    add_row=add_column=int((n-1)/2)  #the number of row and column increase
    new_row=int(row)+int(add_row)*2
    new_column=int(column)+int(add_column)*2
    newimage=np.zeros([new_row,new_column]) #new matrix

    for i in range (add_row,row+add_row):
        for j in range (add_column,column+add_column):
            newimage[i][j]=image[i-add_row][j-add_column]

    for i in range (add_row,row+add_row):
        for j in range (0,add_row):
            newimage[i][j]=image[i-add_row][0]
    for i in range (0,add_row):
        for j in range(add_column,column+add_column):
            newimage[i][j]=image[0][j-add_column]
    for i in range (add_row,row+add_row):
        for j in range (column+add_column,new_column):
            newimage[i][j]=image[i-add_row][column-1]
    for i in range (row+add_row,new_row):
        for j in range (add_column,column+add_column):
            newimage[i][j]=image[row-1][j-add_column]

    file = open('2Dcheck\\PerfectCircleWithTriangle1.pgm', 'w')
    [m, n] = newimage.shape
    max = 2
    file.write('P2\n' + str(n) + ' ' + str(m) + '\n' + str(max) + '\n')
    for i in range(0, m):
        for j in range(0, n):
            file.write(str(int(newimage[i][j])) + '\n')
    file.close()

    # plt.imshow(newimage)
    # plt.show()
    # print(newimage)
    return (newimage)


# border(name='2Dcheck\\PerfectCircleWithTriangle.pgm',n=5,t=1)