% script from W. Birkfellner, M. Figl, J. Hummel: "Medical Image Processing - A Basic Course", copyright 2010 by Taylor & Francis
% preuzeto sa linka: https://s3-eu-west-1.amazonaws.com/s3-euw1-ap-pe-ws4-cws-documents.ri-prod/9781466555570/9781466555570_disc.iso
clear all; close all
img=imread('dtrect.jpg');
distImg=zeros(50,50);
for i=1:50
    for j=1:50
        mindist=71;
        if img(i,j)>0
            for k=-49:49
                for l=-49:49
                    if (i+k)>0 && (i+k)<51 && (j+l)>0 && (j+l)<51
                        if img((i+k),(j+l)) == 0
                            dist=round(sqrt(k*k+l*l));
                            if dist < mindist 
                                mindist=dist;
                            end
                        end
                    end
                end
            end
            distImg(i,j)=mindist;
        end
    end
end
maxint=max(max(distImg));
distImg=distImg/maxint*64;
colormap(gray)
image(distImg)
