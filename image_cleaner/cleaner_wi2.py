#!/usr/bin/env python

import matplotlib.image as im
import numpy as np
import glob
import scipy.misc

indir = '../dat/wi2/'
outdir = '../dat/wi2_clean/'

idx = 1

names = glob.glob(''.join((indir, '*')))

for name in names:
	print(name)

	pic = im.imread(name)
	pic = np.asarray(pic)

	# crop, rm alpha, and scale
	pic = pic[:298, :417, 0:3]
	pic = scipy.misc.imresize(pic, 25) # arg is %

	# write
	#im.imsave(''.join((outdir, str(idx), '.png')), pic)
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)

	# count
	idx += 1

################################################

	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1

	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1
	scipy.misc.imsave(''.join((outdir, str(idx), '.png')), pic)
	idx += 1

