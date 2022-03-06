function dy=feizao(z,y)
g=9.8;
rou=1*10^3;
R=0.001;
gama=35*10^-3;
Bo=rou*g*R^2/gama;
dy=zeros(2,1);
dy(1)=y(2);
dy(2)=(1+y(2)^2)/y(1)-Bo*z*(1+y(2)^2)^1.5;

