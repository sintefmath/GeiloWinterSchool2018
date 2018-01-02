# Geilo Winter School 2018 in eScience - Practical Artificial Intelligence

[Official website](https://www.sintef.no/projectweb/geilowinterschool/)

## Course material

* [course_material](https://github.com/sintefmath/GeiloWinterSchool2018/tree/master/course_material/index.ipynb) - all lessons (run with `jupyter <http://jupyter.org/>`_ to get interactive features)


## Setup

Every participant is asked to perform the following steps prior to attending the winter school.
It consists of installing required packages and downloading datasets that will be used during the school.


### Windows

This tutorial is split into three sections. The first part is installing Anaconda. The second part is testing your installation (making sure conda works, dealing with path issues etc). Finally, the last part of the tutorial goes over installing packages, and environment management. As always, feel free to ask questions either here or on the youtube video page.


1. Go to https://www.anaconda.com/download/#windows and download the python 3.6 version of anaconda.

2. Select the default options when prompted during the installation of Anaconda.

![Add Anaconda to PATH Environmental Variable](https://cdn-images-1.medium.com/max/1600/1*7a9zVyGP3iMXu9aB4e_Vhw.png "Add Anaconda to PATH Environmental Variable")
Add Anaconda to PATH Environmental Variable

Note: If you checked this box, steps 4 and 5are not needed. The reason why it isn’t preselected is a lot of people don’t have administrative rights on their computers.

3. After you finished installing, open Anaconda Prompt. Type the command below to see that you can use a Jupyter (IPython) Notebook.

**jupyter notebook**

If you want a basic tutorial going over how to open Jupyter and using python, please see the [following vide](https://youtu.be/JqGjkNzzU4s).

4. If you didn’t check the add Anaconda to path argument during the installation process, you will have to add python and conda to your environment variables. You know you need to do so if you open a **command prompt** (not anaconda prompt) and get the following messages

![Messages like this mean you havent added python or conda to your path yet. In the next step, we will fix this](https://cdn-images-1.medium.com/max/1600/1*81UWHjyBokvIl8oYI3mafw.png)
Messages like this mean you havent added python or conda to your path yet. In the next step, we will fix this

5. You can add Python and Conda to your path by using the setx command in your command prompt.
![Added Conda and Python to my Environment Variables.](https://cdn-images-1.medium.com/max/1600/1*LJ4T-vEGVjr7K4BfmEXDRQ.png)
Added Conda and Python to my Environment Variables.

If you don’t know where your conda and/or python is, you type the following commands into your anaconda prompt

![You can also manually modify your environment variables.](https://cdn-images-1.medium.com/max/1600/1*JPTn1751dYrPSydYyPXxKg.png)
You can also manually modify your environment variables.

6. Close the current command prompt and open a new one. Try typing python and conda in your command prompt to see if the paths are saved. Done!

### Linux (ubuntu)

Open a [terminal](https://www.howtogeek.com/140679/beginner-geek-how-to-start-using-the-linux-terminal/) and install python 3.6 and pip

```
$ sudo apt-get install python3 python3-pip
$ pip3 install --upgrade pip
```

Install required python packages
```
$ pip3 install numpy jupyter tensorflow keras seaborn numexpr pandas
```


### Mac
