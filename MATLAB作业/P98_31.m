clc;
clear all;


start_time = clock;
a0 = 2; a1 = 1 + sqrt(5); d  = 4;
mu(1) = a0;
mu(2) = a1;
for k = 3:15
    a = a1 + (a1-a0)/d; 
    for i = 1:2
        res = 0.5; der = 0;
        for j = 2:2^(k-1)+1
           der = res*(1-res) + a*(1-2*res)*der;
           res = a*res*(1-res);
        end
        a = a - (res-0.5)/der;
    end
   
    d = (vpa(a1)-vpa(a0))/(vpa(a)-vpa(a1)); 
    fprintf('cishu %u changshu %.15f\n', k, double(d));
    a0 = a1; a1 = a;
    mu(k) = a;
end
end_time = clock;

total_time = end_time - start_time;