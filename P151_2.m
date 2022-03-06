clear all
y1=[];
y2=[];
for x=0.1:0.1:1
    f=quad(@(x) 2*exp(-x.^2)/pi^0.5,0,x);
    y2=[y2 erf(x)];
    y1=[y1 f];
end