path='/Users/xbunax/Downloads/ԭʼ���� ǰ�����ǹ��ղ������������ǹ������ܣ���������Ч�ʡ�����������͸������ 17������(1).xls';
gray=xlsread(path);
a,b=size(gray);
for j=1:b
    gray(:,j)=gray(:,j)/gray(1,j);
end

    