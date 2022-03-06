clear all
x0=pi/4;
n=1;
while n<1000
    n=n+1;
    x0=x0-(exp(x0)-4*cos(x0))/(exp(x0)+4*sin(x0));
end
