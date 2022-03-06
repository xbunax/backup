function dx=mazhikai(t,x)
r1=1;
r2=1;
n1=100;
n2=100;
s1=0.8;
s2=0.7;
dx=zeros(3,1);
dx(1)=x(2);
x(3)=n2*(1-x(1)/n1-x(2)/r1*x(1))/s1;
dx(3)=r2*x(3)*(1-x(3)/n2-s2*x(1)/n1);


