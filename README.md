# 2s986_class



---

## Installation

1. Download and install the [Anaconda python distribution](https://www.anaconda.com/download/), (python3 version, use 64bit unless your machine is old and only supports 32bit). The installation instructions are found [here](https://conda.io/docs/user-guide/install/).

2. Clone demo repository
    * **Windows**
        * Launch `Anaconda Prompt`
        * Type
            ```shell
            git clone https://github.com/PV-Lab/2s986_class.git
            ```
          and press enter (hereafter called "issue" command)
            * If the above command fails with error message `'git' is not recognized ...`, you need to      install `git`. One option is to use `conda` to install `git`: issue
                ```shell
                conda install -c anaconda git
                ```
                Alternatively, check [here](https://git-scm.com/download/win) on installation instructions for `git` on Windows
        * Change directory by issuing
            ```shell
            cd 2s986_class
            ```

    * **MacOS, Linux**
        * Launch a `terminal`
        * Type
            ```shell
            git clone https://github.com/PV-Lab/2s986_class.git
            ```
          and press enter (hereafter called "issue" command)
            * **MacOS:** If you are using Mac OS 10.13 (High Sierra), you may get the error message: `xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools)`. In this case, reinstall xcode by issuing
                ```shell
                xcode-select --install
                ```
                and clone the repository again
        * Change directory by issuing
            ```shell
            cd 2s986_class
            ```

3. Install anaconda:
    * **Note for MacOS/Linux machines**: Check you are indeed using the anaconda binaries by issuing
        ```shell
        which python
        ```
        You should see outputs with something similar to `/User/<your name>/anaconda3/bin/python` (For linux machines, this will be `/home/...` instead of `/User/...`).
        **If you see this, no further action is required**. If instead, you get something like `/usr/bin/python` (i.e. without the anaconda3), you are using your system's python binaries. In this case, please add `/User/<your name>/anaconda3/bin` to your `$PATH` environment variable ([Guide](http://osxdaily.com/2014/08/14/add-new-path-to-path-command-line/)) and then proceed to the next step.

    * **Windows**. In your opened anaconda prompt, issue the following:
        * Create a conda environment:

            ```shell
            conda create -n workshop anaconda pip python=3.6
            ```
            You can use any other name in place of `workshop` but be consistent hereafter
        * Activate the environment:
            ```shell
            activate workshop
            ```
            Your prompt should change, from `C:>` to `(workshop)C:>`

        * Note: you can deactivate the environment by issuing `deactivate`. But make sure to activate the environment again before running any demos from the prompt, since the required packages are installed in this environment! For more information on conda environments, click [here](https://conda.io/docs/user-guide/tasks/manage-environments.html)

    * **MacOS, Linux**. In your opened terminal, issue the following:
        * Create a conda environment:

            ```shell
            conda create -n workshop anaconda pip python=3.6
            ```
            You can use any other name in place of `workshop` but be consistent hereafter
        * Activate the environment:
            ```shell
            source activate workshop
            ```
            Your prompt should change, from `$` to `(workshop)$`

        * Note: you can deactivate the environment by issuing `source deactivate`. But make sure to activate the environment again before running any demos from the terminal, since the required packages are installed in this environment! For more information on conda environments, click [here](https://conda.io/docs/user-guide/tasks/manage-environments.html)


## Getting started

**For demos using `Jupyter notebook`**
    * Launch `Jupyter notebook` ![alt text](https://github.com/acceleratedmaterials/AMDworkshop_demo/blob/master/.pictures/Jupyter.png)
    * Navigate to the `2s986_class` folder
    * Navigate to the corresponding subfolders and click on `<demo name>.ipynb` to begin interacting with the demo ([Guide](https://jupyter-notebook.readthedocs.io/en/stable/))


## License

This project is licensed under the [MIT](LICENSE.md) license.
