[x,t]=dsolve('D2x=g-(k*(Dx)^2*(S-A)-rou*g*S*(x-h))/m','Dh=(A/S)*(2*g*(x-h)+(Dx)^2)^0.5','x(0)=0,h(0)=0','t');
