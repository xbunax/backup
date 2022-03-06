[t,y]=ode45('feizao2',[0 5],[0 0]);
g=9.8;
r=0.01;
gama=32*10^-3;
x=0.025;
m=0.08*10-3;
a=g-2*pi*gama*r*sin(y(:,1)).^2/m;
h=tan(y(:,1)).*(x-r*sin(y(:,1)));
plot(t,h,'-');