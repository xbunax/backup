function da=feizaomo(t,a)
m=0.01;%С������kg
gama=45*10^-3;%��������N*m^-1
g=9.8;%�������ٶ�
r=0.005;%С��뾶m
pi=3.14;
aplha=pi/4;

da=zeros(2,1);
da(1)=a(2);
da(2)=g-2*gama*pi*r*(sin(aplha))^2/m;

%da=zeros(3,1);
%da(1)=a(2);
%a(3)=a(2)*r*sin(a(1));
%da(2)=g/r*sin(a(1))-2*gama*pi*r*sin(a(1))/m*R-a(2)^2*cos(a(1))/sin(a(1));
