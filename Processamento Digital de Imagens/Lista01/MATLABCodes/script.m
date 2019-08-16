%% Script Lista 01
clear all; clc;

f = imread('angiograma-ruido.tif');

% Filtro da mediana

[M,N] = size(f);
g1 = zeros(M+2,N+2); % adiciona borda
g1(2:end-1,2:end-1) = f;

for i=2:M,
    for j=2:N,
        s = sort(reshape(g1(i-1:i+1,j-1:j+1)', 9, 1))';
        g1(i,j) = s(5);
    end
end

g1 = uint8(g1);
size = size(g1);
rows2remove = [1 size(1)];
cols2remove = [1 size(2)];
g1(rows2remove,:)=[];
g1(:,cols2remove)=[];


% Máscara para o laplaciano
w2 = [1 1 1; 1 -8 1; 1 1 1];
l = imfilter(double(g1), w2);
l = uint8(l);
g2 = g1 - l;
g2 = mat2gray(g2);

%Transformação de potência

g3 = double(g2).^(1.1);
g3 = mat2gray(g3);
g3 = im2uint8(g3);

g4 = double(g2).^(1.25);
g4 = mat2gray(g4);
g4 = im2uint8(g4);

g5 = double(g2).^(2);
g5 = mat2gray(g5);
g5 = im2uint8(g5);

figure;
subplot(2,3,1); imshow(f);
subplot(2,3,2); imshow(g1);
subplot(2,3,3); imshow(g2);
subplot(2,3,4); imshow(g3);
subplot(2,3,5); imshow(g4);
subplot(2,3,6); imshow(g5);

figure;
subplot(1,1,1); imshow(g5);

imwrite(g5,'resultado.tif');