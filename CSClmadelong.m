clear all
n = 50;
edge = zeros(n,1);
face = zeros(n,1);
vertex = zeros(n,1);
alpha = zeros(n,1);

for ii = 1:n
    vertex(ii) = 8*(-1)^(ii-1)/sqrt(3*(ii/2)^2);
end

for ii = 2:n
    e = 0;
    for jj = 1 - ii/2 : ii/2 - 1
        e = e+(12*(-1)^(ii - 1))/sqrt(2*(ii/2)^2 + jj^2);
    end
    edge(ii) = e;
end

for ii = 2:n
    f = 0;
    for jj = 1 - ii/2 : ii/2 - 1
        for kk = 1 - ii/2 : ii/2 - 1
            f = f + 6*(-1)^(ii - 1)/sqrt((ii/2)^2 + jj^2 + kk^2);
        end
    end
    face(ii) = f;
end

a = 0; b = 0;
for ii = 1:n 
    a = b + 0.125*vertex(ii) + 0.25*edge(ii) + 0.5*face(ii);
    b = b + vertex(ii) + edge(ii) + face(ii);
    alpha(ii) = sqrt(3)/2 * a;
end
alpha1=sum(alpha)/length(alpha);