import numpy as np
import imageio
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

#%% 
img = Image.open('hequalization_input.png')
img = img.convert('L')

img = np.asarray(img)
img_shape = img.shape
img_size = img_shape[0] * img_shape[1]

hist, bins = np.histogram(img.flatten(), bins=256, range=(0, 255))
cdf = hist.cumsum()
cdf_min = np.min(cdf)

equalized_image = np.zeros_like(img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        equalized_image[i, j] = np.round(255 * (cdf[img[i, j]] - cdf_min) / (img_size - cdf_min))

hist_equalized, bins = np.histogram(equalized_image.flatten(), bins=256, range=(0, 255))

plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.subplot(2, 2, 2)
plt.plot(bins[1:], hist)
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.subplot(2, 2, 4)
plt.plot(bins[1:], hist_equalized)

#%%
img = Image.open('CT.jpg')
img = np.asarray(img)

mask = (img >= 50) & (img <= 100)
img_mask = mask * img

hist, bins = np.histogram(img.flatten(), bins=256, range=(0, 255))
hist_mask, bins = np.histogram(img_mask.flatten(), bins=256, range=(0, 255))

plt.figure()

plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.subplot(2, 3, 2)
plt.plot(bins[1:], hist)

plt.subplot(2, 3, 4)
plt.imshow(img_mask, cmap='gray')
plt.subplot(2, 3, 5)
plt.plot(bins[1:], hist_mask)
plt.subplot(2, 3, 6)
plt.imshow(mask, cmap='gray')

#%%
img = Image.open('CT.jpg')
img = np.asarray(img)

plt.figure()

plt.subplot(2, 4, 1)
plt.imshow(img, cmap='gray')
plt.subplot(2, 4, 5)
mask = (img >= 50) & (img <= 100)
plt.imshow(mask, cmap='gray')

plt.subplot(2, 4, 2)
kernel = np.ones((3, 3)) * 1/9
img_mean = ndi.convolve(img, kernel)
plt.imshow(img_mean, cmap='gray')
plt.subplot(2, 4, 6)
mask = (img_mean >= 50) & (img_mean <= 100)
plt.imshow(mask, cmap='gray')

plt.subplot(2, 4, 3)
img_gaus1 = ndi.gaussian_filter(img, sigma=1)
plt.imshow(img_gaus1, cmap='gray')
plt.subplot(2, 4, 7)
mask = (img_gaus1 >= 50) & (img_gaus1 <= 100)
plt.imshow(mask, cmap='gray')

plt.subplot(2, 4, 4)
img_gaus2 = ndi.gaussian_filter(img, sigma=3)
plt.imshow(img_gaus1, cmap='gray')
plt.subplot(2, 4, 8)
mask = (img_gaus2 >= 50) & (img_gaus2 <= 100)
plt.imshow(mask, cmap='gray')

#%%
img = Image.open('CT.jpg')
img = np.asarray(img)
img_gaus2 = ndi.gaussian_filter(img, sigma=3)
mask = (img_gaus2 >= 50) & (img_gaus2 <= 100)

diff_hor = np.matrix([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
img_diff_hor = ndi.convolve(mask, diff_hor)

diff_ver = np.matrix([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
img_diff_ver = ndi.convolve(mask, diff_ver)

sobel_hor = ndi.sobel(mask, axis=0)
sobel_ver = ndi.sobel(mask, axis=1)
sobel_grad = np.sqrt(sobel_hor**2 + sobel_ver**2)

plt.figure()

plt.subplot(2, 3, 1)
plt.imshow(mask, cmap='gray')

plt.subplot(2, 3, 2)
plt.imshow(img_diff_hor, cmap='gray')

plt.subplot(2, 3, 3)
plt.imshow(img_diff_ver, cmap='gray')

plt.subplot(2, 3, 4)
plt.imshow(sobel_grad, cmap='gray')

plt.subplot(2, 3, 5)
plt.imshow(sobel_hor, cmap='gray')

plt.subplot(2, 3, 6)
plt.imshow(sobel_ver, cmap='gray')