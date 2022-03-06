rou=10^3;
g=9.8;
gama=35*10^-2;
theta=3*pi/4;
R=0.1*10^-2;
B0=rou*g*R^2/gama;
zs=(1-(1+4*B0*(1-cos(theta)))^0.5)/(2*B0);
zmin=0; zmax=zs; Nz=10000;
k=0.45;
z=linspace((zmin/R),(zmax/R),Nz);
hz=((zmax/R)-(zmin/R))/(Nz-1);
u=zeros(1,Nz);
for j=2:Nz-1
    u(end)=sin(theta);
    u(end)=u(end-1)+cot(theta)*hz;
    u(1)=0.3*10^-2;
    u(2)=u(1)+k*hz;
    u(j+1)=(1/(u(j-1)))*(hz)^2*(1+(((u(j)-u(j-1))/hz)^2))-B0*z(j-1)*(hz)^2*(1+(((u(j)-u(j-1))/hz)^2))^1.5+(2*u(j)-u(j-1));
end
plot(u,z)