function dz=houdusakexun1(t,z)
m=0.2;%碗质量/kg
d=0.01;%小孔直径/m
D=0.11;%碗内径/m
D1=1;%水箱内径/m
H=1;%水箱内原始水高
g=9.8;%kg.m/s^2
s1=pi*D1^2/4;%水箱底面积
s=pi*D^2/4;%碗内底面积
A=pi*d^2/4;%小孔面积
rou=10^3;%水密度
C=0.08;%水阻力系数
k=0.5*C*rou;%k=1/2Crou

dz=zeros(3,1);
dz(1)=z(2);
%z(3)=h;
dz(2)=(m*g-k*(z(2))^2*(s-A)-rou*g*s*((s1*z(1)-s1*H+s1*z(3))/(s-s1)))/(m-0.5*rou*s*((s1*z(1)-s1*H+s*z(3))/(s-s1)));
dz(3)=(s/A)*(((H-z(3)-z(1))*2*g*s1)/(s1-s))^0.5;