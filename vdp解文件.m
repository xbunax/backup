[T,Y]=ode15s('vdp1000',[0 3000],[2 0]);
plot(T,Y(:,1),'-')