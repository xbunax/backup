clear all
n=1;
a=pi/4;
b=pi/2;
while n<1000
    n=n+1;
    x0=(a+b)/2;
    if exp(x0)-4*cos(x0)<0
        a=x0;
        b=b;
    else
        b=x0;
        a=a;
    end
end

    