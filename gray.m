path='/Users/xbunax/Downloads/ԭʼ���� ǰ�����ǹ��ղ������������ǹ������ܣ���������Ч�ʡ�����������͸������ 17������(1).xls';
gray=xlsread(path);
a,b=size(gray);
for j=2:b
    gray(:,j)=gray(:,j)/gray(2,j);
end

    