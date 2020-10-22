## Access MaterialsProject.org Dataase 

There are two convenient Python tools to access the database:

1. A convenient wrapper to the Materials API has been implemented in the Python Materials Genomics ([pymatgen](<https://pymatgen.org/>)) library to facilitate researchers in using the MAPI. Please see the [pymatgen wrapper](<https://docs.materialsproject.org/open-apis/the-materials-api/#pymatgen_wrapper>) section.

2. [matminer](<https://hackingmaterials.lbl.gov/matminer/>) is another open-source Python library for performing data mining and analysis in the field of Materials Science. It is meant to make accessible the application of state-of-the-art statistical and machine learning algorithms to materials science data with just a few lines of code.

### Use pymatgen in Python

You can install pymatgen via conda as well via the conda-forge channel on Anaconda cloud:

`conda install --channel conda-forge pymatgen`

If the above fails, try using conda to install some critical dependencies and then do pip install:

`conda install --yes numpy scipy matplotlib`

`pip install pymatgen`

### Use matminer in Python

You can install matminer via conda

 `conda install -c conda-forge pymatgen`
 
Install and update via pip

`pip install matminer`



### API keys from 

To use the Materials API, you need to first have an API key.

(1) Go to [dashboard](<https://materialsproject.org/janrain/loginpage/?next=/dashboard>) to sign in or register with Gmail or Github account;

![alt text](https://github.com/PV-Lab/2s986_class/blob/master/Week8/github1.JPG?raw=true)

(2) When you are at dashboard, click "Generate API Key"

![alt text](https://github.com/PV-Lab/2s986_class/blob/master/Week8/github2.JPG?raw=true)

