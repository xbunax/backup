g=9.8;
rou=1*10^3;
R=0.001;
gama=35*10^-3;
Bo=rou*g*R^2/gama;
fai=0.75*pi;
zs=(1-(1+4*Bo*(1-cos(fai)))^0.5)/(2*Bo);
shijian=[zs 0];
chutiao=[sin(fai) cot(fai)];
[z,y]=ode45('feizao',shijian,chutiao);
plot(y(:,1),z,'-')
