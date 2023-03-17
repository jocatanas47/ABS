clear all
close all

fp=fopen('SKULLBASE.DCM', 'r'); %%%%Može se koristiti i dicomread funkcija u Matlabu (za Octave je neophodno instalirati dodatnu dicom biblioteku)
fseek(fp,1622,'bof');
img=zeros(512,512);
img(:)=fread(fp,(512*512),'short');
img=transpose(img);
fclose(fp);

figure(1); imshow(img,[]); title ('Original')

%% 5x5 Gaussian blur
Kern_Gaus = [1 4 6 4 1; 4 16 24 16 4; 6 24 36 24 16; 4 16 24 16 4; 1 4 6 4 1]/256;
img_Gaus = zeros(512,512);
for i = 3:510
    for j = 3:510
        for cnt1 = -2:2
            for cnt2 = -2:2
                img_Gaus(i,j) = img_Gaus(i,j) + img(i+cnt1,j+cnt2)*Kern_Gaus(cnt1+3,cnt2+3);
            end
        end
    end
end
figure(2); imshow(img_Gaus,[]); title('5x5 Gaussian blur')

%% Sharpening filter
Kern_sharp = [-1 -1 -1; -1 9 -1; -1 -1 -1];
img_sharp = zeros(512,512);
for i = 2:511
    for j = 2:511
        for cnt1 = -1:1
            for cnt2 = -1:1
                img_sharp(i,j) = img_sharp(i,j) + img(i+cnt1,j+cnt2)*Kern_sharp(cnt1+2,cnt2+2);
            end
        end
    end
end
figure (3); imshow(img_sharp,[]); title('Sharpening filter')

%% Kx-forward differentiation
diffimg = zeros(512,512);
for i = 1:511
    for j = 1:512
        diffimg(i,j) = -img(i,j) + img(i+1,j);
    end
end
figure (4); imshow(diffimg,[]); title('Kx-forward differentiation')

%% SOBEL 
Sobel_imgX = zeros(512,512);
Sobel_imgY = zeros(512,512);
Kern_SobX = [-1 -1 -1; 0 0 0; 1 1 1];
Kern_SobY = [-1 0 1; -1 0 1; -1 0 1];
for i = 2:511
    for j = 2:511
        for cnt1 = -1:1
            for cnt2 = -1:1
                Sobel_imgX(i,j) = Sobel_imgX(i,j)+img(i+cnt1,j+cnt2)*Kern_SobX(cnt1+2,cnt2+2);
                Sobel_imgY(i,j) = Sobel_imgY(i,j)+img(i+cnt1,j+cnt2)*Kern_SobY(cnt1+2,cnt2+2);
            end
        end
    end
end
figure (5); imshow(Sobel_imgX,[]); title('Sobel x')
figure (6); imshow(Sobel_imgY,[]); title('Sobel y')

Sobel_img_mag = sqrt(Sobel_imgX.^2+Sobel_imgY.^2);
figure(7); imshow(Sobel_img_mag,[]); title('Sobel')

%% Unsharp masking
Kern_blur = [1 1 1; 1 2 1; 1 1 1]/10;
img_blur = zeros(512,512);
for i = 2:511
    for j = 2:511
        for cnt1 = -1:1
            for cnt2 = -1:1
                img_blur(i,j) = img_blur(i,j) + img(i+cnt1,j+cnt2)*Kern_blur(cnt1+2,cnt2+2);
            end
        end
    end
end
weight = 0.97;
unimg = img - weight*img_blur;
figure(8); imshow(unimg(2:511,2:511),[]); title ('Unsharp masking')


