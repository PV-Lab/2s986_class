import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def RGB_func(t): 
    '''
    This is the 'fake' function to genration RGB from the t_A, t_B, t_C
    Please replace this function with the actual experimental data
    '''
    t = t.dot(np.array([[1,0.1,0.0],[0.0,0.8,0.1],[0.3,0.0,1]]))
    return (t+ 0.02* np.random.randn(*t.shape))*256

def MSE_func(RGB_exp,RGB_ref):
    '''
    Caclulate the metric for optimization: 
    Mean Square Error of experimental RGB measurements and the targeted RGB
    '''
    Y = []
    for i in range(len(RGB_exp)):
        Y.append([mean_squared_error(RGB_exp[i],RGB_ref)])
    return np.array(Y)

def barplot_RGB(RGB_ref,RGB_exp,title_string):
    font = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font)

    plt.bar(np.arange(1)-0.25, [RGB_ref[0]], 0.25,  alpha=1, color='r')
    plt.bar(np.arange(1)-0.00, [RGB_ref[1]] , 0.25,  alpha=1, color='g')
    plt.bar(np.arange(1)+0.25, [RGB_ref[2]], 0.25,  alpha=1, color='b')

    plt.bar(np.transpose(np.arange(1,len(RGB_exp)+1)-0.25), RGB_exp[:,0], 0.25,  alpha=0.5, color='r')
    plt.bar(np.transpose(np.arange(1,len(RGB_exp)+1)+0.00),  RGB_exp[:,1], 0.25,  alpha=0.5, color='g')
    plt.bar(np.transpose(np.arange(1,len(RGB_exp)+1)+0.25), RGB_exp[:,2], 0.25,  alpha=0.5, color='b')
    plt.xticks(np.arange(len(RGB_exp)+1))
    plt.ylabel('RGB values [0 - 256]')
    plt.ylim(0,260)
    plt.title(title_string)
    fig = plt.gcf()
    fig.set_size_inches(10, 4)
    plt.show()

def MSE_RGB_3Dplot(X, Y, title_string):
    font = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = ax.scatter(X[:,0], X[:,1], X[:,2], c=np.squeeze(np.sqrt(Y)), linewidth=3,vmin=0, vmax=50)#plt.hot())
    cbar = fig.colorbar(img, pad=0.2)
    cbar.set_label('RGB RMSE')
    ax.set_xlabel('Liquid A (µL)',labelpad=10)
    ax.set_ylabel('Liquid B (µL)',labelpad=10)
    ax.set_zlabel('Liquid C (µL)',labelpad=10)
    ax.set_xlim3d(0, 200)
    ax.set_ylim3d(0, 200)
    ax.set_zlim3d(0, 200)
    ax.set_title("RMSE vs Amounts of Liquid A, B, C")
    ax.view_init(30, 360-60)
    fig.set_size_inches(7, 4.5)
    plt.show()

    
def get_dispense_positions(start_pos, batch_size):
    row_num=8
    col_num=12
    row_dict = {"A": 0, "B": 1, "C": 2, "D":3, "E":4, "F":5, "G":6, "H": 7,
                0: "A", 1: "B", 2: "C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H"}
    row_ind = row_dict[start_pos[0]]
    col_ind = int(start_pos[1:])
    dispense_pos = []
    for i in range(batch_size):
        if col_ind <=col_num:
            dispense_pos.append(row_dict[row_ind]+str(col_ind))
        else:
            col_ind = col_ind-12
            row_ind = row_ind+1
            dispense_pos.append(row_dict[row_ind]+str(col_ind))
        col_ind = col_ind+1
    return dispense_pos