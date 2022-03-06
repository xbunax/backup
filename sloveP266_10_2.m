
[t,y1]=ode23('P266_10_2',[0,1],[1]);
plot(t,y1,'x')
hold on 
[t,y2]=ode23s('P266_10_2',[0,1],[1]);
plot(t,y2,'o')
