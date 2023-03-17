close all
clear all
img = imread('MouseCT.jpg');

figure(1)
imshow(img)
title ('Original image')

fimg = fftshift(fft2(img));

gs=zeros(733,733);
sigma=3;
for j=1:733
for k=1:733
gs(j,k)=exp(-((j-366)^2+(k-366)^2)/(2*sigma^2));
end
end

gs=fftshift(fft2(gs));

fimg_filt=gs.*fimg;

cimg=ifftshift(ifft2(fimg_filt));

minint=min(min(cimg));
cimg=cimg-minint;
maxint=max(max(cimg));
cimg=cimg/maxint*64;

figure(2)
colormap(gray);
image(abs(cimg))
title ('Gaussian low pass filter')