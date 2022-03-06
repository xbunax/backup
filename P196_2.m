clear all
X=[-3 -2 0 3 4];
Y=[18 10 2 2 5];
p=polyfit(X,Y,2);
a=-3:0.1:4;
y=polyval(p,a);
plot(a,y,X,Y,'r*')