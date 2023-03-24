import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

plt.close('all')

# ZADATAK 1

img = np.loadtxt('matrix_slajs_200.txt')

img_niz = img.flatten()
plt.figure()
his = ndi.histogram(img_niz, 0, 1600, 1600)
plt.plot(his)
plt.title('Histogram originalne slike')

img_median = ndi.median_filter(img, size=3)
plt.figure()
plt.imshow(img_median, cmap='gray')
plt.title('Nakon median filtra')

mask = (img_median>=400) & (img_median<=1015) 
plt.figure()
plt.imshow(mask, cmap='gray')
plt.title('Maska')

mask_erode = ndi.binary_erosion(mask,iterations=15)

mask_dil = ndi.binary_dilation(mask_erode, iterations=15)
plt.figure()
plt.imshow(mask_dil, cmap='gray')
plt.title('Maska nakon morfoloskih operacija')

labels, nlabels = ndi.label(mask_dil)
print('Broj objekata: ',nlabels)
overlay = np.where(labels>0, labels, np.nan)
plt.figure()
plt.imshow(overlay, cmap='rainbow')
plt.title('Objekti')

# ZADATAK 2
plt.figure()
plt.imshow(img, cmap='gray')
plt.imshow(overlay, cmap='rainbow', alpha=0.15)

objekti = ndi.find_objects(labels)
plt.figure()
roi = img[objekti[1]]
plt.imshow(roi)
plt.title('Pravougaona ROI oko izdvojenog objekta')

roi_niz = roi.flatten()
plt.figure()
his_roi = ndi.histogram(roi_niz, 0, 1600, 1600)
plt.plot(his_roi)
plt.title('Histogram pravougaone ROI')

sr_vred = ndi.mean(roi)
print('Srednja vrednost: ', sr_vred)
std = ndi.standard_deviation(roi)
print('Standardna devijacija: ', std)


# ZADATAK 3

lv_val = labels[68, 225]      # nalazenje labele za srce
lv_mask = np.where(labels == lv_val,1,0)

dist_trans = ndi.distance_transform_edt(lv_mask)
dist_max = ndi.maximum(dist_trans)
print('Maksimalno rastojanje: ', dist_max)
dist_min = ndi.minimum(dist_trans)
max_position = ndi.maximum_position(lv_mask)
print('Pozicija tacke koja ima max. rastojanje: ', max_position)

lv_mask1 = np.where(labels == lv_val,1,np.nan)

plt.figure()
plt.imshow(img, cmap='gray')
plt.imshow(lv_mask1, cmap='rainbow', alpha=0.15)
centar = ndi.center_of_mass(lv_mask)
print('x koordinata centra: ', centar[1], '    y koordinata centra: ', centar[0])
plt.scatter(centar[1], centar[0], s=10, c='red', marker='x')
plt.show()

plt.figure()
plt.imshow(img, cmap='gray')
plt.show()
plt.imshow(dist_trans, cmap='hot', alpha=0.6)
plt.title('Slika rastojanja')











