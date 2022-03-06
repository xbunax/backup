d=0.1;
lamda=400*10^-9;
k=2*pi/lamda;
x=-0.001:0.000003:0.001;y=x;
e2=sqrt(2/lamda/d);
x1=e2.*x;
for n=1:667
    l(n)=abs(F(x1(n)))+sqrt(0.5)*exp(1i.*pi./4);
    f(n)=F(x1(n));
    E=sqrt(0.5)*exp(1i*(k*d-pi/4))*(F(x1(n))+sqrt(0.5)*exp(1i*pi/4));
    I3(n)=abs(E);
end
H=max(I3);
xmax=find(I3(:)==H);
xm=xmax*0.000003-0.001;
plot(f);
hold on 
figure
plot(x,I3);
[X,Y]=meshgrid(x,y);
L=repmat(I2,[677,1]);
figure
hold on
mesh(L);