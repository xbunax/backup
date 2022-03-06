[x,y]=meshgrid(-2:0.1:2,-2:0.1:2);
z=1./sqrt((x-1).^2+y.^2+0.01)-1./sqrt((x+1).^2+y.^2+0.01);
[px,py]=gradient(z);
contour(x,y,z,[-12,-8,-5,-3,-1,-0.5,-0.1,0.1,0.5,1,3,5,8,12])
hold on
quiver(x,y,px,py,'k')
    