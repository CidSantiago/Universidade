%% Criação da Imagem
% 256 tons de cinza

img = zeros(256, 256);
i = 0;

for n = 1:256
    for m = 1:256
        img(m,n) = i;
    end
    i = i + 1;
end

img = mat2gray(img);
imwrite(img,'imagemteste.tif')