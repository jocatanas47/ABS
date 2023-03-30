import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
import os

plt.close("all")

im = imageio.imread('IM-0001-0001.DCM')

print(type(im))
print(im.shape)
print(im[0,0])
print(im[11:14,290:293])
print(im.meta)
print(im.meta.keys())
print(im.meta['Modality'])
print(im.meta['sampling'])

plt.figure()
plt.imshow(im, cmap = 'gray')
plt.axis('off')

plt.figure()
plt.imshow(im, cmap = 'rainbow')
plt.axis('off')

#%%

im2 = imageio.imread('IM-0001-0002.DCM')
im3 = imageio.imread('IM-0001-0003.DCM')

niz = np.stack((im, im2, im3))
print(niz.shape)

#%%
# print(os.listdir('CT HEAD-NK 5.0 B30s'))
vol_83 = imageio.volread('CT HEAD-NK 5.0 B30s', 'dcm')
print(vol_83.shape)
d0, d1, d2 = vol_83.meta['sampling']
print(d0)
print(d1)
print(d2)

print(d0 * d1 * d2)

#%%
fig, axes = plt.subplots(nrows=3, ncols=3)

# frontalni
axes[0, 0].imshow(vol_83[:, 256, :], cmap='gray')
axes[0, 0].axis('off')

for i in range(3):
    for j in range(3):
        axes[i, j].axis('off')
        
# frontalni
axes[0, 1].imshow(vol_83[:, 256, :], cmap='gray', aspect=d0/d2)
# transverzalni
axes[1, 1].imshow(vol_83[40, :, :], cmap='gray', aspect=d1/d2)
# sagitalni
axes[2, 1].imshow(vol_83[:, :, 256], cmap='gray', aspect=d0/d1)

im = imageio.imread('imageinverse_input.png')[:, :, 0]
plt.figure()
plt.imshow(im, cmap = 'gray')
imageio.imwrite('slika.jpg', im)