clear all
vp=1578;
f1=quad(@(v) 4.*v.^2.*exp(-v.^2/vp^2)/((pi)^0.5*vp^3),0,vp);
f2=quad(@(v) 4.*v.^2.*exp(-v.^2/vp^2)/((pi)^0.5*vp^3),0,3.3*vp);
f3=quad(@(v) 4.*v.^2.*exp(-v.^2/vp^2)/((pi)^0.5*vp^3),3e4,3e8);

