clear;
close all;
clc;

fpointer = fopen('PIG_MR', 'r');
fseek(fpointer, 8446, 'bof');
img = zeros(512, 512);
img(:) = fread(fpointer, (512*512), 'short');
img = transpose(img);
rhomax = max(max(img))
rhomin = min(min(img))
newimg = zeros(512,512);
newimg = (img-rhomin)/(rhomax-rhomin)*256;
colormap(gray)
image(newimg)
% imwrite(newimg, "nova1", "pgm") %unrecognized suffix

%%
fp = fopen('SKULLBASE.DCM', 'r');
fseek(fp, 1622, 'bof');
img = zeros(512,512);
img(:) = fread(fp, (512*512), 'short');
img = transpose(img);
fclose(fp);
minint = min(min(img));
img = img - minint + 1;
img = log(img);
maxint = max(max(img));
img = img/maxint*256;
colormap(gray)
image(img)

%%
oimg = imread('ABD_CT.jpg');
size(oimg)
pomega = 127;
psigma = 25;
sigmoid = zeros(256,1);
for rho=0:255
    sigmoid(rho+1, 1) = 256/(1+exp(-((rho-pomega)/psigma)));
end
figure(1)
plot(sigmoid)
transimage = zeros(261,435);
for i = 1:261
    for j = 1:435
        rho = oimg(i, j);
        transimage(i, j) = sigmoid(rho+1,1);
    end
end
figure(2)
subplot(1,2,1)
colormap(gray)
image(transimage)
subplot(1,2,2)
colormap(gray)
image(oimg)

%% Histogram 
img = imread('ABD_CT.jpg');
depth = max(max(img))-min(min(img))
hist16 = zeros(16,1);
for i = 1:261
    for j = 1:435
        rho = img(i, j);
        b16 = floor(rho/17.0)+1;hist16(b16,1) = hist16(b16,1)+1;
    end
end
figure()
bar(hist16)
save('Histogram16.txt', 'hist16', '-ascii');