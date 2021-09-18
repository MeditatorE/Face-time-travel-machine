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


