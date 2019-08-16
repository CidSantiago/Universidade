function [img] = halftoning(m,n,img,img0)
%HALFTONING Converte uma imagem PB em padrão halftone
%   Converte cada pixel da imagem, que se encontra na
%   escala cinza de 0 a 255, em uma matriz 3x3 de pixels
%   pretos e brancos. Os diferentes tons de cinza são
%   representados a partir da densidade de pixels pretos.

center = [ (m*3)-1 (n*3)-1];

if img0(m,n)>= 0 && img0(m,n)<=0.10
    img(center(1)-1,center(2)-1) = 0;
    img(center(1)-1,center(2)) = 0;
    img(center(1)-1,center(2)+1) = 0;
    img(center(1),center(2)-1) = 0;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 0;
    img(center(1)+1,center(2)-1) = 0;
    img(center(1)+1,center(2)) = 0;
    img(center(1)+1,center(2)+1) = 0;
elseif img0(m,n)>0.10 && img0(m,n)<=0.2
    img(center(1)-1,center(2)-1) = 0;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 0;
    img(center(1),center(2)-1) = 0;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 0;
    img(center(1)+1,center(2)-1) = 0;
    img(center(1)+1,center(2)) = 0;
    img(center(1)+1,center(2)+1) = 0;
elseif img0(m,n)>0.20 && img0(m,n)<=0.3
    img(center(1)-1,center(2)-1) = 0;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 0;
    img(center(1),center(2)-1) = 0;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 0;
    img(center(1)+1,center(2)-1) = 0;
    img(center(1)+1,center(2)) = 0;
    img(center(1)+1,center(2)+1) = 1;
elseif img0(m,n)>0.30 && img0(m,n)<=0.4
    img(center(1)-1,center(2)-1) = 1;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 0;
    img(center(1),center(2)-1) = 0;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 0;
    img(center(1)+1,center(2)-1) = 0;
    img(center(1)+1,center(2)) = 0;
    img(center(1)+1,center(2)+1) = 1;
elseif img0(m,n)>0.40 && img0(m,n)<=0.5
    img(center(1)-1,center(2)-1) = 1;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 0;
    img(center(1),center(2)-1) = 0;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 0;
    img(center(1)+1,center(2)-1) = 1;
    img(center(1)+1,center(2)) = 0;
    img(center(1)+1,center(2)+1) = 1;
elseif img0(m,n)>0.50 && img0(m,n)<=0.6
    img(center(1)-1,center(2)-1) = 1;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 1;
    img(center(1),center(2)-1) = 0;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 0;
    img(center(1)+1,center(2)-1) = 1;
    img(center(1)+1,center(2)) = 0;
    img(center(1)+1,center(2)+1) = 1;
elseif img0(m,n)>0.60 && img0(m,n)<=0.7
    img(center(1)-1,center(2)-1) = 1;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 1;
    img(center(1),center(2)-1) = 0;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 1;
    img(center(1)+1,center(2)-1) = 1;
    img(center(1)+1,center(2)) = 0;
    img(center(1)+1,center(2)+1) = 1;
elseif img0(m,n)>0.70 && img0(m,n)<=0.8
    img(center(1)-1,center(2)-1) = 1;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 1;
    img(center(1),center(2)-1) = 0;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 1;
    img(center(1)+1,center(2)-1) = 1;
    img(center(1)+1,center(2)) = 1;
    img(center(1)+1,center(2)+1) = 1;
elseif img0(m,n)>0.80 && img0(m,n)<=0.9
    img(center(1)-1,center(2)-1) = 1;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 1;
    img(center(1),center(2)-1) = 1;
    img(center(1),center(2)) = 0;
    img(center(1),center(2)+1) = 1;
    img(center(1)+1,center(2)-1) = 1;
    img(center(1)+1,center(2)) = 1;
    img(center(1)+1,center(2)+1) = 1;
else
    img(center(1)-1,center(2)-1) = 1;
    img(center(1)-1,center(2)) = 1;
    img(center(1)-1,center(2)+1) = 1;
    img(center(1),center(2)-1) = 1;
    img(center(1),center(2)) = 1;
    img(center(1),center(2)+1) = 1;
    img(center(1)+1,center(2)-1) = 1;
    img(center(1)+1,center(2)) = 1;
    img(center(1)+1,center(2)+1) = 1;
end

