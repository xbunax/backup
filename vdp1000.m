function dy=vdp1000(t,y)
w=195;%jiaosudu
b=y(1)/0.16;%x0/H0
A=6.5*10^-3;%振幅
g=9.8;%重力加速度
rou=10^3;%密度
H0=0.16;%高度/m
Pe=10^5;%压强p
vb0=0.1*10^-6;
R0=2.9*10^-3;
wp=A*w^2/g;%AW^2/g
vp=rou*H0*g/Pe;%rou*H0*g/Pe 
%Pe=10^5 H0=0.16 Vb0=0.1*10^-6 R0=2.9*10^-3 A=6.5mm W=195 1/s
vb=vb0*(1-vp*b-vp*b*wp*sin(w*t));
vbt=vb0*(-vp*y(1)/0.16-vp*wp*w*cos(w*t)*b-vp*y(1)*24.45*sin(w*t)/0.16);
rb=R0*(1-vp*b/3-vp*b*wp*sin(w*t)/3);
m=0.001;
dy=zeros(2,1);
dy(1)=y(2);
dy(2)=(-1*(0.5*rou*y(1)*vbt)-4*rou*rb^2*0.2*y(1)^2*sign(y(1))+(m-rou*vb)*(A*w^2*sin(w*t)+g))/(0.5*vb*rou+m);

