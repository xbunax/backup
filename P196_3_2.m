clear all
y=[];
x=-0.2:0.1:1;
for i=x
    a=2*i^5-3*i^3-i^2-9;
    y=[y a];
end
y=y+0.1*rand(1,13);
p=polyfit(x,y,5);
p1=polyval(p,x);
xx=-0.2:0.01:1;
pp1=pchip(x,y,xx);
plot(xx,pp1,x,p1)
hold on