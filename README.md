# Face-time-travel-machine
This project use to implement Face-Aging with cycleGAN.


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
cd Face-time-travel-machine-main
```

2. Install Anaconda

   [**https://www.anaconda.com**](https://www.anaconda.com)

3. Install pytorch 0.4+
```
pip install pytorch
```

4. Install dominate>=2.3.1
```
pip install dominate
```

## Start
We have saved the trained parameters in the [**checkpoints**](https://github.com/MeditatorE/Face-time-travel-machine/tree/main/checkpoints/aging_cyclegan) and can call it directly through the GUI to generate pictures.

### If you are using Mac OS
Run [**main.py**](https://github.com/MeditatorE/Face-time-travel-machine/blob/main/main.py) directly to start.
```
python main.py
```

### If you are using Windows
Run [**window_main.py**](https://github.com/MeditatorE/Face-time-travel-machine/blob/main/window_main.py) directly to start.
```
python window_main.py
```
Then follow the Demo:

![](https://github.com/MeditatorE/Face-time-travel-machine/blob/main/Demo/QQ20210918-220741-HD.gif)

Or you can download the [**Demo video**](https://github.com/MeditatorE/Face-time-travel-machine/blob/main/Demo/Face%20Time%20Travel%20Machine.mp4).


### If you don't want to use the saved parameters
You can choose your own training data.

Run [**train.py**](https://github.com/MeditatorE/Face-time-travel-machine/blob/main/train.py) to start.
```
python train.py --dataroot ./datasets/young2old --name aging_cyclegan --model cycle_gan
```

# Results
## Young to old
              Input                         Output                     reconstruction 


<img width="781" alt="截屏2021-09-18 下午10 17 20" src="https://user-images.githubusercontent.com/90904086/133891903-964bf9d5-cb82-4950-98e3-a497d6a8a7ab.png">
<img width="781" alt="截屏2021-09-19 下午1 37 53" src="https://user-images.githubusercontent.com/90904086/133917066-a290d132-092d-4cb7-ab64-4d9c0239b926.png">
<img width="782" alt="截屏2021-09-19 下午1 40 19" src="https://user-images.githubusercontent.com/90904086/133917109-2cf7b525-a455-4745-aba4-4fcbf59efc42.png">

## Old to young
              Input                         Output                     reconstruction 
<img width="780" alt="截屏2021-09-19 下午1 52 06" src="https://user-images.githubusercontent.com/90904086/133917068-28ea9061-4ef7-464f-a481-46aef5c9d671.png">
<img width="783" alt="截屏2021-09-19 下午1 52 48" src="https://user-images.githubusercontent.com/90904086/133917061-92e34095-c3a5-430a-b6ee-051f4713c467.png">
<img width="782" alt="截屏2021-09-18 下午10 17 44" src="https://user-images.githubusercontent.com/90904086/133891928-d6ffff3c-1bcd-4184-8294-647f9eaee61c.png">


## Improvement and optimization
On the whole, the model is more friendly to Europeans and Americans, and the effect is not good for other ethnic minorities. We think this is due to the high proportion of Europeans and Americans in the training concentration. After testing, we found that if we use the training set of a certain ethnic group, the training model will significantly improve the aging / rejuvenation effect of the model on this ethnic group.


## Summary
* [**Final summary**]

## References
* [**CycleGAN paper**](https://arxiv.org/abs/1703.10593)
* [**pytorch-CycleGAN-and-pix2pix**](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) 
