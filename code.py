import imageio as ii
import numpy as np

img = ii.imread('imageEmbedded.png')
img = img << 6
img = img.astype(np.uint8)
ii.imsave('result.png', img)