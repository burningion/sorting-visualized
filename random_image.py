import numpy as np
from PIL import Image

from skimage import color
from scipy.misc import imsave

import random

newImage = np.random.randint(0, 255, (300, 300, 3))

testImage = Image.fromarray(newImage.astype("uint8"))
testImage.save('testing.png')

for i in range(newImage.shape[0]):
    newImage[i,:,0] = np.sort(newImage[i,:,0])

testImage = Image.fromarray(newImage.astype("uint8"))
testImage.save('testing_sorted_r.png')


for i in range(newImage.shape[0]):
    newImage[i,:,1] = np.sort(newImage[i,:,1])

testImage = Image.fromarray(newImage.astype("uint8"))
testImage.save('testing_sorted_g.png')

for i in range(newImage.shape[0]):
    newImage[i,:,2] = np.sort(newImage[i,:,2])

testImage = Image.fromarray(newImage.astype("uint8"))
testImage.save('testing_sorted_b.png')

from skimage import color
from scipy.misc import imsave

import numpy as np

newImage = np.random.randint(0, 255, (300, 300, 3))

in_hsv_h = color.convert_colorspace(newImage, 'RGB', 'HSV')
in_hsv_s = in_hsv_h.copy()
in_hsv_v = in_hsv_h.copy()

for i in range(newImage.shape[0]):
    in_hsv_h[i,:,0] = np.sort(in_hsv_h[i,:,0])
    in_hsv_s[i,:,1] = np.sort(in_hsv_s[i,:,1])
    in_hsv_v[i,:,2] = np.sort(in_hsv_v[i,:,2])
imsave('testing-sorted-hue.png', color.convert_colorspace(in_hsv_h, 'HSV', 'RGB'))
imsave('testing-sorted-saturation.png', color.convert_colorspace(in_hsv_s, 'HSV', 'RGB'))
imsave('testing-sorted-value.png', color.convert_colorspace(in_hsv_v, 'HSV', 'RGB'))

from skimage import color
from scipy.misc import imsave

import numpy as np

img = np.zeros((300, 300, 3), dtype='float32') # hsv works in range from 0 - 1

for i in range(img.shape[1]):
    img[:,i,:] = i / img.shape[1], 1.0, 1.0

in_rgb = color.convert_colorspace(img, 'HSV', 'RGB')
imsave('initial_hsv_1.png', in_rgb)

for i in range(img.shape[0]):
    np.random.shuffle(img[i,:,:])

imsave('initial_hsv_1_shuffled.png', color.convert_colorspace(img, 'HSV', 'RGB'))
