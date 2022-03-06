clc;
clear;
x=cplxgrid(20);
y=exp(1j*x);
figure();
subplot(1,2,1)
cplxmap(x,y)
subplot(1,2,2)
cplxmap(x,x.^0.2)
hold on
