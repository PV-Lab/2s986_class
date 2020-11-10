import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from datetime import datetime


def image_extractor(file_name):
    pic_folder = '.\\data\\'
    # Read all the files from a specified directory
    for img in os.listdir('.\\data\\'):
        if img.endswith(file_name):
            #files.append(dirpath+filename)
            image = Image.open(pic_folder+img, 'r')
            im = Image.fromarray(np.array(image, dtype=np.uint8), 'RGB')
            # Create figure and axes
#             fig,ax = plt.subplots(1,figsize=(8,8))
#             # Display the image
#             ax.imshow(im)
#             plt.show()            
    #%%
    # test picture for adjusting the cropping box
    # should try mutiple ones for the optimium cropping box options
    def find_coeffs(pa, pb):
        matrix = []
        for p1, p2 in zip(pa, pb):
            matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
            matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

        A = np.matrix(matrix, dtype=np.float)
        B = np.array(pb).reshape(8)

        res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
        return np.array(res).reshape(8)

    img = image
    width, height = img.size
    m = -0.1
    n = 0.1
    xshift = abs(m) * width
    yshift = abs(n) * height
    new_width = width + int(round(xshift))
    new_height = height +int(round(yshift))

    coeffs = find_coeffs(
            [(0, 0), (640, 0), (640, 480), (0, 480)],
            [(110, 100), (480, 0), (525, 305), (209, 295)])

    img_corr = img.transform((int(width*1.05), int(height*1.4)), Image.PERSPECTIVE, coeffs, Image.BICUBIC)

#     # Create figure and axes
#     fig,ax = plt.subplots(1,figsize=(7,7))
#     # Display the image
#     ax.imshow(img_corr)
#     plt.show()

    #crop_box= (430, 15, 610, 150) #well plate
    crop_box= (443, 15, 615, 145) #flat plate

    image_cropped = img_corr.crop(box=crop_box) #box=(left, upper, right, lower)

    def get_image_array(image, crop_box):
        """Get a numpy array of an image so that one can access values[x][y]."""
        image = image.crop(box=crop_box) #box=(left, upper, right, lower)
        [width,height] = image.size
        pixel_values = list(image.getdata())
        if image.mode == 'RGB':
            channels = 3
        elif image.mode == 'L':
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
            return None
        pixel_values = np.array(pixel_values).reshape((height, width, channels))
        return (width,height,pixel_values)

    def image_slicing(image_array, col_num,row_num, offset_array):
        """slice the ROIs from an image of an array of samples/colorcard"""
        row_h = image_array.shape[0]/row_num#int(np.round(image_array.shape[0]/row_num))

        col_w = image_array.shape[1]/col_num#int(np.round(image_array.shape[1]/col_num))

        fig,ax = plt.subplots(1,figsize=(8,8))
        images = []
        imagecol = []
        for y in np.arange(row_num):
            imagerow = []
            for x in np.arange(col_num):
                # slicing indices for each color square
                y1 = int(np.round(row_h*y+offset_array[1][0]))
                y2 = int(np.round(row_h*(y+1)-offset_array[1][1]))
                x1 = int(np.round(col_w*x+offset_array[0][0]))
                x2 = int(np.round(col_w*(x+1)-offset_array[0][1]))
                image = image_array[y1:y2,x1:x2]
                imagerow.append(image)#append every images in a row into a row list
                images.append(image)#append every images into a list
                # Add the rectangular patch to the Axes
                # Create a Rectangle patch
                lw=1 # Line width
                ec='r' # edge color
                fc='none' # face color
                rect = patches.Rectangle((x1,y1),x2-x1,y2-y1,
                                          linewidth=lw,edgecolor=ec,facecolor=fc)
                ax.add_patch(rect)

            imagecol.append(np.concatenate(imagerow, axis=1))
        image_reconstr = np.array(np.concatenate(imagecol, axis=0), dtype=np.uint8)

        return [fig, ax, image_reconstr, images]

    w, h, image_array = get_image_array(img_corr, crop_box)

    # Row, Columns Settings and Offset pixels for each sample (TO BE CHANGED)
    row_num=8
    col_num=12
    offset_array= [[3,3],[3,3]]#[[x_left,x_right],[y_upper,y_lower]]
    ########%%%%%%%%%%%%%%%%%%%%%%%%###############
    [fig_ROI, ax_ROI, reconstr_ROI, image_ROI]= image_slicing(
            image_array, col_num, row_num, offset_array)
    ax_ROI.imshow(Image.fromarray(np.array(image_array, dtype=np.uint8), 'RGB'))
    plt.show()
    
    return image_ROI

def get_rgb_from_samples(image_ROI, sample_pos):
    
    row_num=8
    col_num=12
    row_dict = {"A": 0, "B": 1, "C": 2, "D":3, "E":4, "F":5, "G":6, "H": 7,
                 0: "A", 1: "B", 2: "C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H"}
    
    start_pos = sample_pos[0]
    row_ind = row_dict[start_pos[0]]
    col_ind = int(start_pos[1])
    sample_indx = (row_num*col_num-1) - (row_ind*col_num+(col_ind-1)+np.arange(len(sample_pos)))

    rgb_list = []
    n_fig = 10
    for n in np.arange(0, int((len(sample_indx)-1)/n_fig)*n_fig+1, n_fig):
        fig,axes = plt.subplots(2, n_fig, figsize=(2.5*n_fig, 4))
        for i in np.arange(n_fig):
            if n< len(sample_indx):
                img_sample = image_ROI[sample_indx[n]]
                [r,g,b] = [np.median(img_sample[:,:,0]),np.median(img_sample[:,:,1]),np.median(img_sample[:,:,2])]
                rgb_list.append([r,g,b])
                axes[0,i].imshow(img_sample)
                axes[0,i].set_xlim(2,7)
                axes[0,i].set_ylim(2,7)
                axes[1,i].imshow([[[int(r),int(g),int(b)]]])
                axes[1,i].set_title('RGB:'+str([int(r),int(g),int(b)]), fontsize = 12)

                axes[0,i].set_axis_off()
                axes[1,i].set_axis_off()
            else:
                axes[0,i].imshow([[[int(255),int(255),int(255)]]])
                axes[0,i].set_xlim(2,7)
                axes[0,i].set_ylim(2,7)
                axes[1,i].imshow([[[int(255),int(255),int(255)]]])


                axes[0,i].set_axis_off()
                axes[1,i].set_axis_off()
            n = n+1
        fig.tight_layout(pad= 0.3)
        plt.show()
    return np.array(rgb_list)