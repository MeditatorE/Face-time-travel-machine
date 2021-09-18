# Face-time-travel-machine
This project use to implement Face-Aging with cycleGAN


## Abstract
In this project, we explored the technical principles, wide applications and technical features of GAN, and chose CycleGAN among many models to achieve rejuvenation and aging of faces. We trained the model with the largest dataset available on the web and found shortcomings from the original very mature dataset and reference projects, and independently produced the dataset for testing to corroborate our conjectures, finally tried to solve them in the process of reproducing the application.


## Contribution
This repo is heavily based on [**Original CycleGAN implementation**](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). Most of our work involves search data sets, adjust model parameters to better generate images, and write code for image processing and GUI.


## Data Process & Datesets
### Training dataset
Our training data comes from [**IMDB-WIKI-500k+ face images with age and gender labels**](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/). The training set is already provided in the folder [**datasets**](https://github.com/MeditatorE/Face-time-travel-machine/tree/main/datasets/young2old). We sorted the images in the Wiki-IMDB dataset by age, then selected 4600 images from the 20s and 50s+ images as our dataset, removed undersized images and grayscale images, and adjusted all images to 256 × 256. The relevant code is provided in [**data process**](https://github.com/MeditatorE/Face-time-travel-machine/tree/main/data%20process).

### Testing dataset
The [**testing set**](https://github.com/MeditatorE/Face-time-travel-machine/tree/main/datasets/young2old/test%20dataset) is also collected from the wiki-IMDB dataset and processed in the same way as the training set.

In addition, we found that the model generally had a better effect on European and American people, but not on Asian, African and other ethnic minorities. Therefore, we created a test set of [**Asian pictures**](https://github.com/MeditatorE/Face-time-travel-machine/tree/main/datasets/young2old/Asian%20test%20dataset) to specifically explore relevant issues. The Asian test set used 112 images collected from the Internet, which were also processed into 256 × 256 images.


## About cycleGAN
### What is cycleGAN?
Cyclegan is essentially two mirror symmetrical Gan, forming a ring network. Two Gan share two generators and each has a discriminator, that is, there are two discriminators and two generators. One unidirectional GaN has two losses, that is, there are four losses in total.
![5806754-895305b01b041acc](https://user-images.githubusercontent.com/90904086/133890083-1cfe039a-7a45-4501-879a-41d432aa2ebf.png)

![5806754-c32814397100c895](https://user-images.githubusercontent.com/90904086/133890088-be6a1151-134b-4d3b-8041-aa9443697d34.png)

### Why cycleGAN? 
Obtaining photos taken by a person at different ages is both challenging and expensive, so we chose to use cyclegan to implement this project. Because cyclegan can transfer domain knowledge between groups without paired input and output examples. Cyclegan can capture the facial features of young people's portraits in an image set and find out how to apply these features to facial images in the elderly set.


# Getting Started
## Installation
1. Clone this repo
```
git clone https://github.com/MeditatorE/Face-time-travel-machine.git    
cd Face-time-travel-machine
```

2. Install Anaconda

   [**https://www.anaconda.com**](https://www.anaconda.com)

3. Install pytorch 0.4+
```
pip install pytorch
```

## Start
We have saved the trained parameters in the [**checkpoints**](https://github.com/MeditatorE/Face-time-travel-machine/tree/main/checkpoints/aging_cyclegan) and can call it directly through the GUI to generate pictures.

Run [**main.py()**](https://github.com/MeditatorE/Face-time-travel-machine/blob/main/main.py) directly to start.
```
python main.py
```
Then follow the Demo:
![](https://github.com/MeditatorE/Face-time-travel-machine/blob/main/Demo/QQ20210918-215314-HD.gif)
