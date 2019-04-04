Next in-person Bootcamp: 3-7 June, San Francisco. [Register here](https://bootcamp.zerotodeeplearning.com)

------

[![Build Status](https://travis-ci.org/zerotodeeplearning/intro_deep_learning_one_day.svg?branch=master)](https://travis-ci.org/zerotodeeplearning/intro_deep_learning_one_day)


# TDWI Intro to Deep Learning

Hands-on Introduction to Deep Learning with Python and Tensorflow


## Quick start guide

#### Download and Install Anaconda Python 3.7

The first step is to download and install Python 3 on your system, together with all the necessary libraries. Luckily for us Anaconda provides a convenient way to do so. Download and install it here:

https://www.anaconda.com/download

Next we are going to download the code and access the notebooks. The following commands should be run from a terminal.


#### Install Tensorflow

There are 2 ways to do this:

1) from the Anaconda package manager choose Tensorflow and install it
2) open an Anaconda prompt and type `conda install tensorflow`

#### Clone this repository on your local computer
```
git clone https://github.com/zerotodeeplearning/intro_deep_learning_one_day.git
```

> TIP: If you are not familiar with git and github you can just download the zip file of the repository.

#### Change to course folder

```
cd intro_deep_learning_one_day
```

> TIP: If you downloaded the zip file and not the repo, your folder name will be `intro_deep_learning_one_day_master`, just cd into that one: `cd intro_deep_learning_one_day_master`

#### Launch Jupyter Notebook

From the course folder, in the terminal, type:
```
jupyter notebook
```
If the command is not recognized try to close and open the terminal again, maybe the path needs to be updated after installation.

> TIP: You can also launch Jupyter using the Anaconda Launcher. This will open Jupyter at your default Home location and you will have to manually navigate to the course folder.

#### Open your browser to

If it didn't open automatically, you can find Jupyter at the following url:
```
http://localhost:8888
```

You are good to go! Enjoy!



### Instructions for Conda environment creation

The following is not necessary if you have a recent version of Anaconda installed on your computer. If you want to create a virtual environment specifically for this tutorial, we provide an [environment configuration file](environment.yml). From the terminal follow these steps:

#### Change to course folder

```
cd intro_deep_learning_one_day
```

#### Create the course environment

```
conda env create
```

wait for the environment to create, this may take a few minutes

#### Activate the environment (Mac/Linux)

```
conda activate ztdloneday
```

#### Activate the environment (Windows)

```
activate ztdloneday
```

Check that your prompt changed to

```
(ztdloneday) $
```

Now you can run jupyter notebook from within the environment.



### Troubleshooting

#### Updating Conda

If you have installed Anaconda a long time ago, you may want to update it by running

```
conda update conda
```

and then

```
conda update anaconda
```
