import imageio
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi  

plt.close('all')

########### Ucitavanje JPG slike
img = imageio.imread('CT.jpg')
plt.figure()
plt.imshow(img, cmap = 'gray')
plt.title('CT originalna slika')

# Python zadatak 1/3 sa prethodnog časa
niz = img.flatten()

plt.figure()
hist = ndi.histogram(img, 0, 256, 256)
plt.plot(hist)
plt.title('Histogram originalne slike')

mask = (img>50) & (img<100)
im_mask=np.where (mask,img,0)

plt.figure()
plt.imshow(im_mask, cmap = 'gray')
plt.title('Maskirana slika')
plt.figure()
hist = ndi.histogram(im_mask, 0, 256, 256)
plt.plot(hist)
plt.title('Histogram maskirane slike')

plt.figure()
plt.imshow(mask, cmap = 'gray')
plt.title('Maska')

#kraj zadatka sa prethodnog časa

# Python zadatak - morfologija
dil_slika = ndi.binary_dilation(mask, iterations=5)
plt.figure()
plt.imshow(dil_slika, cmap = 'gray')
plt.title('Maska - dilatacija')

zat_slika = ndi.binary_closing(dil_slika,iterations=5)
plt.figure()
plt.imshow(zat_slika, cmap = 'gray')
plt.title('Maska - zatvaranje')






