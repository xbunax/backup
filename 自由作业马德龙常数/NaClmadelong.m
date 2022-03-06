clear all
a=0;
b=100;
for i=-b:b
    i2=i*i;
    for j=-b:b
        j2=i2+j*j;
        for k=-b:b
            if i~=0||j~=0||k~=0
             
                if mod(i+j+k,2)==0
                    a=a+(j2+k*k)^-0.5*(-1);
                else 
                    a=a+(j2+k*k)^-0.5*1;
                end
                
            end
        end
    end
end

    
                
                
    
        