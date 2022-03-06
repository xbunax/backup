function dy=lotka(t,y)
alpha=0.01;
dy=zeros(2,1);
dy(1)=2*y(1)-alpha*y(1)*y(2);
dy(2)=-y(2)+alpha*y(1)*y(2);
