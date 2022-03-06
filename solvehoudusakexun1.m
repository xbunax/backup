[t,z]=ode45('houdusakexun1',[0 2],[1 0 0]);
plot(t,z(:,1),'-')
ylabel('x/m')
xlabel('t/s')

%1. x-t
%2. v-t
%3. h-t