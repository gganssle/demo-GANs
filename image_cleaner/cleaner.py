#!/usr/bin/env python

import matplotlib.image as im
import numpy as np
import glob

indir = '../dat/webpage_images/'
outdir = '../dat/webpage_images_clean/'

idx = 1

names = glob.glob(''.join((indir, '*')))

for name in names:
	#print(name)

	pic = im.imread(name)
	pic = np.asarray(pic)

	# crop and rm alpha
	pic = pic[:298, :417, 0:3]

	# write
	im.imsave(''.join((outdir, str(idx), '.png')), pic)

	# count
	idx += 1

