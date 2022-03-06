path='/Users/xbunax/Downloads/原始数据 前五列是工艺参数，后三列是过滤性能（包括过滤效率、过滤阻力、透气量） 17个样本.xlsx';
x=xlsread(path);
[r,a]=size(x);
xmin=[];
xmax=[];
y=zeros(r,a);
for j=1:a
    xmin(end+1)=min(x(:,j));
    xmax(end+1)=max(x(:,j));
end
for k=1:a
    for l=1:r
        y(l,k)=(x(l,k)-xmin(k))/(xmax(k)-xmin(k));
    end
end
u=zeros(r,5);
for j=2:6
    for k=1:r
        u(k,j-1)=((y(k,j)-y(1,j)))^2;
    end
end
delatay=zeros(r,3);
for j=7:9
    for k=1:r
        delatay(k,j-6)=abs((y(k,j)-y(1,j)));
    end
end
sumu=[];
for j=1:5
    sumu(end+1)=sum(u(:,j));
    sumu(j)=sqrt(sumu(j)-u(1,j));
end
sumdelatay=[];
for n=1:3
    sumdelatay(end+1)=sum(delatay(:,n));
end
    