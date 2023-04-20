from PIL import Image
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

plt.close('all')

#%% 1. ucitavanje, reskaliranje i prikaz

im = imageio.imread('PET_snimak.dcm')
im = Image.fromarray(im)

im_resized = im.resize((1024, 1024))

im = np.asarray(im)
im_resized = np.asanyarray(im_resized)

plt.figure()

plt.subplot(1, 2, 1)
plt.imshow(im, cmap='gray')
plt.title('originalna slika')

plt.subplot(1, 2, 2)
plt.imshow(im_resized, cmap='gray')
plt.title('resemplovana slika')

#%% 2.popravka kvaliteta

im_filtered = im_resized
im_filtered = ndi.gaussian_filter(im_filtered, sigma=5)
im_filtered = ndi.median_filter(im_filtered, size=3)
kernel = np.matrix([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
im_filtered = ndi.convolve(input=im_filtered, weights=kernel)

plt.figure()

plt.subplot(1, 2, 1)
plt.imshow(im_resized, cmap='gray')
plt.title('originalna slika')

plt.subplot(1, 2, 2)
plt.imshow(im_filtered, cmap='gray')
plt.title('filtrirana slika')

#%% 3. segmentacija

plt.figure()

mask = im_filtered > 700
plt.subplot(1, 3, 1)
plt.imshow(mask, cmap='gray')
plt.title('segmentacija')

mask = ndi.binary_erosion(input=mask, iterations=3)
plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title('erozija')

mask = ndi.binary_dilation(input=mask, iterations=3)
plt.subplot(1, 3, 3)
plt.imshow(mask, cmap='gray')
plt.title('dilatacija')

#%% 4. prikaz

overlay = np.where(mask == True, True, np.nan)

plt.figure()
plt.imshow(im_resized, cmap='gray')
plt.imshow(overlay, alpha=0.5)
plt.title('segmentirani tumor')

im_segmented = np.where(mask == True, im_resized, 0)

#%% 5. cuvanje

imageio.imwrite('1.jpg', im_resized)
imageio.imwrite('2.jpg', im_filtered)
mask = np.where(mask == True, 1, 0)
imageio.imwrite('3.jpg', mask)
imageio.imwrite('4.jpg', im_segmented)