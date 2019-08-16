%% Halftoning
% Recebendo nome da imagem
img0 = strtrim(input('Imagem: ', 's'));
% Recebendo configuração da impressora
resol = input('Resolução de impressão (DPI): '); % em dpi

tamanho = [11 8.5]; % em polegadas [altura largura]
% Limite do tamanho da impressão
limite = resol .* tamanho; % em pixels
% Lendo imagem
img0 = imread(img0);

% Conversão da imagem RGB --> PB
if (ndims(img0) == 3)
  img0 = rgb2gray(img0);
end

img0 = mat2gray(img0);
len = size(img0); % tamanho da imagem de entrada
lenOut = 3*len; % tamanho da imagem de saída

% Atribuindo a uma nova variável para que
% não se perca a imagem original em cinza
imgP = img0;

% Razão entre a possível imagem de saída e o limite
razao = lenOut ./ limite;

% Caso o tamanho da imagem seja maior que o limite
% um redimensionamento é aplicado.
if max(razao) > 1
  fprintf('Imagem muito grande. Será aplicado redimensionamento.\n');
  fprintf('Razão do redimensionamento: %f\n', 1/max(razao));
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
