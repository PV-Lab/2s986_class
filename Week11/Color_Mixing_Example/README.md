### What are the files in this folder?
`ssh_command.py` - the ssh commands for OT2 robot

`color_mixing.py` - the python Protocol (i.e., the execution sequence) for OT2 robot

`utils.py` - some functions for plotting and other tasks

`image_process.py` - image processing functions to extract RGB values from a camera image

`gpyopt_optimizer.py` - BO optimizer which uses GPyOpt API (if you want to use BO, check it out here.)

`color_mixing_with_BO.iphynb` - one example code that will be used to run your algorithm 


### If you decided to use GPyOpt, you need to install it. (Of course, you don't need to use GPyOpt.)
One tip is to install Emukit (another implenmentation of BO) first:

`pip install emukit`

Then, install GPyOpt

`pip install GPyOpt`

This is the werid but effective way we found that solves a package dependence issue on scipy version. Both GPyOpt and Emukit are the BO wrapper based on GPy.

You might need to install C++ editor or compilers if the error prompts during installation.


### Please, please pay attentions about the data structure 

X = [[1,2,3],[1,2,3],[1,2,3]] #liquid dispensing amount
RGB outputs = [[255,255,255],[255,255,255],[255,255,255]]
Y = [[1],[1],[1]]




