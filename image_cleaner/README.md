# NOTE:

When using the `soumith` [version](https://github.com/soumith/dcgan.torch) of the DCGAN, the images have to go in as 3 tensors. When you `matplotlib.im.imsave` a .png file, you save a 4 tensor. Hence the use of `scipy.misc.imsave` in `cleaner.py`.
