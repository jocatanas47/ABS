close all
clear all
img = imread('MouseCT.jpg');

figure(1)
subplot(1,2,1);
imshow(img)
title ('Original image')

fimg = fft2(img);
fimg_abs=abs(fimg);
fimg_shift = fftshift(fimg_abs);
f=log(fimg_shift);

minint=min(min(f));
f=f-minint;
maxint=max(max(f));
f=f/maxint*64;

subplot(1,2,2);
image(f)
title ('2D Fourier transform of image')
colormap gray

