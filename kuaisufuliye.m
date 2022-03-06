I=imread('/Users/xbunax/Desktop/cupt/20年/10石墨导线/表征/IMG_5424.JPG');
F=fft2(im2double(I));
F=fftshift(F);
F=real(F);
T=log(F+1);
subplot(1,2,1),imshow(I),title('原始图像');
subplot(1,2,2),imshow(T,[]),title('原始图像其频谱图');
