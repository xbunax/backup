function dz=sakexun(t,z)
m=0.5;
g=9.8;
d=0.005;
D=0.11;
s=pi*D^2/4;
A=pi*d^2/4;
rou=10^3;
C=0.08;
k=0.5*C*rou;
dz=zeros(3,1);
dz(1)=z(2);
%z(3)=h;
dz(3)=(A/s)*(2*g*(z(1)-z(3))+z(2)^2)^0.5;
dz(2)=g-(k*z(2)^2*(s-A)+rou*g*s*(z(1)-z(3)))/m;





