clear all
x0=pi/4;
x1=pi/2;
n=1;
while n<5
    n=n+1;
    x2=x1-(exp(x1)-4*cos(x1))*(x1-x0)/(exp(x1)-4*cos(x1)-exp(x0)+4*cos(x0));
    x0=x1;
    x1=x2;
    
end
