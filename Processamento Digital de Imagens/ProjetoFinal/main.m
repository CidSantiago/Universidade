%% Halftoning
% Recebendo nome da imagem
img0 = strtrim(input('Imagem: ', 's'));
% Recebendo configura��o da impressora
resol = input('Resolu��o de impress�o (DPI): '); % em dpi

tamanho = [11 8.5]; % em polegadas [altura largura]
% Limite do tamanho da impress�o
limite = resol .* tamanho; % em pixels
% Lendo imagem
img0 = imread(img0);

% Convers�o da imagem RGB --> PB
if (ndims(img0) == 3)
  img0 = rgb2gray(img0);
end

img0 = mat2gray(img0);
len = size(img0); % tamanho da imagem de entrada
lenOut = 3*len; % tamanho da imagem de sa�da

% Atribuindo a uma nova vari�vel para que
% n�o se perca a imagem original em cinza
imgP = img0;

% Raz�o entre a poss�vel imagem de sa�da e o limite
razao = lenOut ./ limite;

% Caso o tamanho da imagem seja maior que o limite
% um redimensionamento � aplicado.
if max(razao) > 1
  fprintf('Imagem muito grande. Ser� aplicado redimensionamento.\n');
  fprintf('Raz�o do redimensionamento: %f\n', 1/max(razao));
  imgP = imresize(imgP, 1/max(razao));
  len = size(imgP);
  lenOut = 3*len;
end

% Criando matriz para nova imagem
imgF = zeros(lenOut(1),lenOut(2));

% Construindo nova imagem
for m = 1:len(1)
    for n =  1:len(2)
        %progresso = 100*(((m - 1)*len(2) + n)/(len(1)*len(2)));
        %fprintf("%.2f%% \n", progresso);
        imgF = halftoning(m,n,imgF,imgP);
    end
end

figure(); imshow(imgF);
