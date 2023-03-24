% script from W. Birkfellner, M. Figl, J. Hummel: "Medical Image Processing - A Basic Course", copyright 2010 by Taylor & Francis
% preuzeto i modifikovano sa linka: https://s3-eu-west-1.amazonaws.com/s3-euw1-ap-pe-ws4-cws-documents.ri-prod/9781466555570/9781466555570_disc.iso

clear all; close all; clc;
img = imread('evil.jpg');
img = img - min(img(:));
img = round(img/max(img(:)));

figure; imshow(img,[]);

himg = zeros(360,439);
for i = 1:310
    for j = 1:310
        if img(i,j)>0
            for ang = 1:360
                theta = ang*pi/180;
                r = round(i*cos(theta)+j*sin(theta));
                if r>0
                    himg(ang,r) = himg(ang,r)+1;
                end
            end
        end
    end
end
figure; image(himg'); colormap(gray); set(gca, 'YDir','normal'); 

perc = 10;
maxint = max(himg(:));
for i = 1:360
    for j = 1:439
        if himg(i,j) > maxint - maxint*perc/100
            himg(i,j) = 64;
        else
            himg(i,j) = 0;
        end
    end
end

figure; image(himg'); colormap(gray); set(gca, 'YDir','normal'); 

transimg = zeros(310,310);
for maxphi = 1:360
    for maxr = 1:439
        if himg(maxphi,maxr) > 0
            normalvect = zeros(1,2);
            normalvect(1,1) = maxr*cos((maxphi)*pi/180);
            normalvect(1,2) = maxr*sin((maxphi)*pi/180);
            unitvect = normalvect*[0 1; -1 0];
            unitvect = unitvect/sqrt(unitvect*unitvect');
            
            len = 0;
            i = round(normalvect(1,1));
            j = round(normalvect(1,2));
            while (i>1 && i<309 && j>1 && j<309)
                i = round(normalvect(1,1)+len*unitvect(1,1));
                j = round(normalvect(1,2)+len*unitvect(1,2));
                transimg(i,j) = 64;
                len = len+1;
            end
            
            unitvect = -unitvect;
            len = 0;
            i = round(normalvect(1,1));
            j = round(normalvect(1,2));
            while (i>1 && i<309 && j>1 && j<309)
                i = round(normalvect(1,1)+len*unitvect(1,1));
                j = round(normalvect(1,2)+len*unitvect(1,2));
                transimg(i,j) = 64;
                len = len+1;
            end
        end
    end
end
figure; colormap(gray); image(transimg);