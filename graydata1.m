path='/Users/xbunax/Downloads/ԭʼ���� ǰ�����ǹ��ղ������������ǹ������ܣ���������Ч�ʡ�����������͸������ 17������.xlsx';
gray=xlsread(path);
[a,b]=size(gray);
for j=7:b
    gray(:,j)=gray(:,j)/gray(1,j);
end
for j=7:b
    gray(:,j)=gray(:,j)/mean(gray(:,j));
end
ck=gray(:,6);%�ڶ���
cp=gray(:,7:end);
cp_index_num=size(cp,2);

%�Ƚ϶�����ο��������
for j = 1:cp_index_num
    t(:,j)=cp(:,j)-ck;
end
%���������С��
mmax=max(max(abs(t)));
mmin=min(min(abs(t)));
rho=0.5;
%3�������ϵ��
ksi=((mmin+rho*mmax)./(abs(t)+rho*mmax));

%4���������
ksi_column_num=size(ksi,1);
r=sum(ksi,1)/ksi_column_num;

%5�����������򣬵õ����r3>r2>r1
[rs,rind]=sort(r,'descend');


