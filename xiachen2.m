function dy=xiachen2(t,y)
w=195;%jiaosudu
A=6.5*10^-3;%振幅
g=9.8;%重力加速度
rou=10^3;%密度
H0=0.16;%高度/m
b=y(1)/H0;%gaodubi
Pe=10^5;%压强p
vb0=0.1*10^-6;%体积
R0=2.9*10^-3;%半径
xp=0.5;%粘滞系数
m=0.0009;%质量
wp=A*w^2/g;%AW^2/g
vp=rou*H0*g/Pe;%rou*H0*g/Pe 
%Pe=10^5 H0=0.16 Vb0=0.1*10^-6 R0=2.9*10^-3 A=6.5mm W=195 1/s

dy=zeros(2,1);
dy(1)=y(2);
E0=-vp*xp*rou*vb0*y(2)/H0;
E1=-vp*wp*xp*rou*vb0*y(2)/H0;
G1=-vp*wp*xp*rou*vb0*w*b;
C0=(m-rou*vb0*(1-vp*b))*g;
C1=(m-rou*vb0*(1-2*vp*b))*A*w^2;
C2=rou*vb0*vp*b*wp*A*w^2;
D0=m+xp*rou*vb0*(1-vp*b);
D1=-vp*wp*xp*rou*vb0*b;
Fx=4*rou*R0^2*0.2*y(2)^2*sign(y(2));
dy(2)=(-1*(E0+E1*sin(w*t)+G1*cos(w*t))*y(2)-Fx+C0+C1*sin(w*t)+C2*sin(w*t)^2)/(D0+D1*sin(w*t));

