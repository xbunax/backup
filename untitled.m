x=[0.0962,0.1924,0.2886,0.3848];
x1=1:1:4;
y=[0.00037,0.00074,0.00111,0.00148];
p=polyfit(x,y,1);

m=[0.09,0.13,0.2,0.31];
n=[0.00037,0.00074,0.00111,0.00148];
error1=[0.00002368,0.000239982,0.00034077,2.87712E-05];
q1=polyfit(m,n,1);

a=[0.09,0.23,0.31,0.36];
b=[0.00037,0.00074,0.00111,0.00148];
error2=[0.000168461,0.000183076,0.000082362,0.00005698];
q2=polyfit(a,b,1);

c=[0.14,0.24,0.31,0.37];
d=[0.00037,0.00074,0.00111,0.00148];
error3=[0.000023828,0.000144596,0.000082362,0.000095312];
q3=polyfit(c,d,1);

plot(x,y);
errorbar(c,d,error3);
set(gca,'FontSize',18);
set(gca,'xTickLabel',num2str(get(gca,'xTick')','%.2f'))
hold on
scatter(c,d);
%plot(q3,c);
%plot(m,n,'o',m,polyval(q1,m));
%hold on
%plot(a,b,'o',a,polyval(q2,a));
plot(polyval(q3,c));
xlabel('x/mm')
ylabel('F/N')
title('F=kx')
legend('F=kx','ÊµÑé3ÄâºÏ','location','SouthEast')

