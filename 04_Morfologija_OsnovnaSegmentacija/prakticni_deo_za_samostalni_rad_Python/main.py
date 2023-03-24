import numpy as np
import imageio
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

#%%
img = Image.open('CT.jpg')
img = np.asarray(img)

mask = (img >= 50) & (img <= 100)
img_dilated = ndi.binary_dilation(mask, iterations=5)
img_closed = ndi.binary_closing(mask, iterations=5)

plt.figure()

plt.subplot(1, 3, 1)
plt.imshow(mask, cmap='gray')
plt.subplot(1, 3, 2)
plt.imshow(img_dilated, cmap='gray')
plt.subplot(1, 3, 3)
plt.imshow(img_closed, cmap='gray')

#%%
img = np.loadtxt('matrix_slajs_200.txt')

hist = ndi.histogram(input=img, min=0, max=1600, bins=1600)

img_medi_filt = ndi.median_filter(img, size=3)

mask = (img_medi_filt >= 400) & (img_medi_filt <= 1000)

mask_processed = ndi.binary_erosion(input=mask, iterations=17)
mask_processed = ndi.binary_dilation(input=mask_processed, iterations=17)

labels, nlabels = ndi.label(mask_processed)
overlay = np.where(labels > 0, labels, np.nan)

plt.figure()
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.subplot(2, 3, 2)
plt.plot(hist)
plt.subplot(2, 3, 3)
plt.imshow(img_medi_filt, cmap='gray')
plt.subplot(2, 3, 4)
plt.imshow(mask, cmap='gray')
plt.subplot(2, 3, 5)
plt.imshow(mask_processed, cmap='gray')
plt.subplot(2, 3, 6)
plt.imshow(overlay, cmap='rainbow')

#%%
objects = ndi.find_objects(labels)

roi = img[objects[1]]

roi_array = roi.flatten()

roi_hist = ndi.histogram(roi_array, 0, 1600, 1600)

roi_mean = ndi.mean(roi)
roi_std = ndi.standard_deviation(roi)

plt.figure()
plt.imshow(img, cmap='gray')
plt.imshow(overlay, cmap='rainbow', alpha=0.15)

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(roi, cmap='gray')
plt.subplot(1, 2, 2)
plt.plot(roi_hist)

print(roi_mean)
print(roi_std)

#%%
overlay = np.where(labels == 2, 1, 0)

img_center = ndi.center_of_mass(overlay)

img_distance_transform = ndi.distance_transform_edt(overlay)

overlay = np.where(labels == 2, 1, np.nan)

dist_max = ndi.maximum(img_distance_transform)
max_position = ndi.maximum_position(img_distance_transform)

plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(img, cmap='gray')
plt.imshow(overlay, cmap='rainbow', alpha=0.15)
plt.scatter(img_center[1], img_center[0], s=10, c='red', marker='x')
plt.subplot(2, 1, 2)
plt.imshow(img, cmap='gray')
plt.imshow(img_distance_transform, cmap='hot', alpha=0.4)

print(dist_max)
print(max_position)

