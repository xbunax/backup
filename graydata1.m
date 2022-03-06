path='/Users/xbunax/Downloads/原始数据 前五列是工艺参数，后三列是过滤性能（包括过滤效率、过滤阻力、透气量） 17个样本.xlsx';
gray=xlsread(path);
[a,b]=size(gray);
for j=7:b
    gray(:,j)=gray(:,j)/gray(1,j);
end
for j=7:b
    gray(:,j)=gray(:,j)/mean(gray(:,j));
end
ck=gray(:,6);%第二列
cp=gray(:,7:end);
cp_index_num=size(cp,2);

%比较队列与参考队列相减
for j = 1:cp_index_num
    t(:,j)=cp(:,j)-ck;
end
%求最大差和最小差
mmax=max(max(abs(t)));
mmin=min(min(abs(t)));
rho=0.5;
%3、求关联系数
ksi=((mmin+rho*mmax)./(abs(t)+rho*mmax));

%4、求关联度
ksi_column_num=size(ksi,1);
r=sum(ksi,1)/ksi_column_num;

%5、关联度排序，得到结果r3>r2>r1
[rs,rind]=sort(r,'descend');


