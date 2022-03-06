[t,z]=ode45('xiaosais',[0 0.25],[0 0 0 0.1 0]);
plot(t,z(:,1),'-')