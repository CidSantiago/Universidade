%% Script Lista 02
%% Questao 1
clear all; clc;

forig1 = imread('imagens-lista2/orig_chest_xray.tif');
f1 = double(forig1);
PQ = paddedsize(size(f1));
F = fft2(f1, PQ(1), PQ(2));

% Filtro passa-alta gaussiano 
D0 = 40;
H = hpfilter('gaussian', PQ(1), PQ(2), D0);
G1 = H.* F;
g1 = ifft2(G1);
g1 = uint8(g1);
g1 = g1(1:size(f1,1),1:size(f1,2));
g1 = histeq(g1);

% Filtra de alta ênfase

G2 =(0.5 + 0.75 .* H ).* F;
g2 = ifft2(G2);
g2 = uint8(g2);
g2 = g2(1:size(f1,1),1:size(f1,2));

% Equalização de histograma
g3 = histeq(g2);

figure;
subplot(2,2,1); imshow(forig1);
subplot(2,2,2); imshow(g1);
subplot(2,2,3); imshow(g2);
subplot(2,2,4); imshow(g3);

%% Questão 2

forig2 = imread('imagens-lista2/car_75DPI_Moire.tif');
f2 = double(forig2);
t2 = fft2(f2);
PQ2 = paddedsize(size(f2));
F2 = fft2(f1, PQ2(1), PQ2(2));

p1 = fftshift(t2); % Center FFT
p1 = abs(p1); % Get the magnitude
p1 = log(p1+1); % Use log, for perceptual scaling, and +1 since log(0) is undefined
p1 = mat2gray(p1); % Use mat2gray to scale the image between 0 and 1
figure;
subplot(1,4,1);imshow(forig2);
subplot(1,4,2);imshow(p1);

D0 = 3; n = 4;
H = lpfilter('btw', PQ2(1), PQ2(2), D0, n);
G21 = H.* F2;
g21 = ifft2(G21);
g21 = uint8(g21);
g21 = g21(1:size(f2,1),1:size(f2,2));

p2 = fftshift(G21); % Center FFT
p2 = abs(p2); % Get the magnitude
p2 = log(p2+1); % Use log, for perceptual scaling, and +1 since log(0) is undefined
p2 = mat2gray(p2);

subplot(1,4,3); imshow(p2);
subplot(1,4,4); imshow(g21);
