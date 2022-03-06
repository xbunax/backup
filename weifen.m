function dy=weifen(t,x)
dy=zeros(2,1);
dy(1)=x(2);
dy(2)=sin(t)-x(2)-x(1);
