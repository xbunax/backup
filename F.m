function CS=F(a)
CS=integral(@fun1,0,a);
function fun=fun1(u)
fun=cos(0.5.*pi.*u.^2)+1i.*sin(0.5*pi.*u.^2);
