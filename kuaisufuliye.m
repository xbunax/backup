I=imread('/Users/xbunax/Desktop/cupt/20��/10ʯī����/����/IMG_5424.JPG');
F=fft2(im2double(I));
F=fftshift(F);
F=real(F);
T=log(F+1);
subplot(1,2,1),imshow(I),title('ԭʼͼ��');
subplot(1,2,2),imshow(T,[]),title('ԭʼͼ����Ƶ��ͼ');
