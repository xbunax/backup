syms y(x)
Dy=diff(y);
D2y=diff(y,2);
w=195;%jiaosudu
A=6.5*10^-3;%���
g=9.8;%�������ٶ�
rou=10^3;%�ܶ�
H0=0.16;%�߶�/m
Pe=10^5;%ѹǿp
vb0=0.1*10^-6;%���
R0=2.9*10^-3;%�뾶
xp=0.5;%ճ��ϵ��
m=0.001;%����
wp=A*w^2/g;%AW^2/g
vp=rou*H0*g/Pe;%rou*H0*g/Pe 
s=dsolve('D2y=(-1*((-vp*xp*rou*vb0*Dy/H0)+(-vp*wp*xp*rou*vb0*Dy/H0)*sin(w*t)+(-vp*wp*xp*rou*vb0*w*y/H0)*cos(w*t))*Dy-(4*rou*R0^2*0.2*Dy^2*sign(Dy))+((m-rou*vb0*(1-vp*y/H0))*g)+((m-rou*vb0*(1-2*vp*y/H0))*A*w^2)*sin(w*t)+(rou*vb0*vp*(y/H0)*wp*A*w^2)*sin(w*t)^2)/((m+xp*rou*vb0*(1-vp*y/H0))+(-vp*wp*xp*rou*vb0*y/H0)*sin(w*t))','y(0)=0.04','Dy(0)=7.8','t');
