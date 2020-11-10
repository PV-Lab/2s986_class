### What are the files in this folder?
`ssh_command.py` - the ssh commands for OT2 robot

`color_mixing.py` - the python Protocol (i.e., the execution sequence) for OT2 robot

`utils.py` - some functions for plotting and other tasks

`image_process.py` - image processing functions to extract RGB values from a camera image

`gpyopt_optimizer.py` - BO optimizer which uses GPyOpt API (if you want to use BO, check it out here.)

`color_mixing_with_BO.iphynb` - one example code that will be used to run your algorithm 


### If you decided to use GPyOpt, you need to install it. (Of course, you don't need to use GPyOpt or Emukit. But, inform us in advance if you are using special packages.)
One tip is to install Emukit (another implenmentation of BO) first:

`pip install emukit`

Then, install GPyOpt

`pip install GPyOpt`

This is the werid but effective way we found that solves a package dependence issue on scipy version. Both GPyOpt and Emukit are the BO wrapper based on GPy.

You might need to install C++ editor or compilers if the error prompts during installation.


### Please pay attentions to the data structure described below when reading the example code. 

You only need to write code to define 4 things

#### intial conditions
X_init = [[50,50,100],[50,50,100],[50,50,100]] #liquid dispensing amount for initial sampling. The sum of the three values in each [] must be 200 uL

#### optimizaiton metric 
Y = [[1],[1],[1]] #the optimization metric/error function, which is defines the difference between RGB_exp to RGB_ref

RGB_exp = [[255,255,255],[255,255,255],[255,255,255]] #the color outputs for sampples 

RGB_ref = [[10,10,10]] #the color outputs for referenece. 


#### subsequent conditions
X_New = [[50,50,100],[50,50,100]] #liquid dispensing amount for subsequent sampling. The sum of the three values in each [] must be 200 uL


#### when to stop 
for i in range(20): ## 20 subsequent runs ## you should implement an early break in the for loop 
