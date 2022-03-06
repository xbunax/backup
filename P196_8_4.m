clear all
a=fzero(@(x) fun(x),[pi/4 pi/2]);
function y=fun(x)
y=exp(x)-4*cos(x);
end