clc;
clear;
a=[];
for x=1:100
    y=x^2+sin(x)+log(x);
    a=[a y];
end