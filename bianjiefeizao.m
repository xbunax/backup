solinit=bvpinit(linspace(0,10,10),[1 0.001]);
sol=bvp4c(@feizao,@twobc,solinit);
x=linspace(0.001,1);
y=deval(sol,x);
plot(x,y(1,:));
fai=pi/4;
function dy=feizao(z,y)
g=9.8;
rou=1*10^3;
R=0.001;
gama=45*10^-3;
Bo=rou*g*R^2/gama;
dy=zeros(2,1);
dy(1)=y(2);
dy(2)=(1+y(2)^2)/y(1)-Bo*z*(1+y(2)^2)^1.5;
end
function res=twobc(ya,yb)
res=[ya(1)-10,yb(1)-sin(pi/4)];
end
