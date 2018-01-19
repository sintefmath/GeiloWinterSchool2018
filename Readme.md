# Geilo Winter School 2018 in eScience - Practical Artificial Intelligence

[Official website](https://www.sintef.no/projectweb/geilowinterschool/)

## Course material

[course_material](https://github.com/sintefmath/GeiloWinterSchool2018/tree/master/course_material/index.ipynb)


## Setup

Every participant is asked to perform the following steps prior to attending the winter school.
It consists of installing required packages and downloading datasets that will be used during the school.

### Installing python

Go to https://www.anaconda.com/download/ and download the python 3.6 version of anaconda for your operating system.

Test your installation by first opening "Anaconda promt" (found on your start menu, windows does a search if you start typing with the start menu open). This should open a terminal in which you can type "python". If the installation was successful you will see something along the lines of

```
(C:\Users\kjetil\AppData\Local\Continuum\anaconda3) C:\Users/kjetil> python
Python 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or license" for more infomration.
>>>
```
Type `exit()` and press enter

### Installing required packages

Start "Anaconda Promt" if you haven't already (see above) and type the following
```
pip install numpy scipy matplotlib pandas keras seaborn numexpr sklearn tensorflow
```

In addition you will need either `opencv-python` or `pygame` to access the webcam (either will work). Depending on your operating system we recoomend:

#### Windows or Mac
`pip install opencv-python`

#### Linux
`pip install pygame`


### Downloading course material

* [Download](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/sintefmath/GeiloWinterSchool2018) the source materials for this course and extract it someplace on your computer.
* [Cats and dogs](https://www.dropbox.com/s/5dx3zcoxgytihlj/cats_dogs.zip?dl=0) the cats vs dogs dataset (20,000 images of cats and dogs for classification)
* [Ships](https://www.dropbox.com/s/s7wb8jdkjextf12/shipsnet.json.zip?dl=0#) 2800 colour images of aerial view of ships


### Follow the lectures

Open "Jupyter Notebook" (found on the start menu after installing anaconda). This opens a tab in your web-browser. Navigate to the folder where you extracted the course material and open the file `course_material/index.ipynb`

