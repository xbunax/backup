clc;
clear;
A=magic(3);
a=triu(A);%��������
b=tril(A);%��������
c=[sum(A(1,:)) sum(A(2,:)) sum(A(3,:))];%����
d=[sum(A(:,1)) sum(A(:,2)) sum(A(:,3))];%����
e=median(A);%����Ԫ��
f=diag(A);%��������
g=A';%��������
h=fliplr(A);%��������
i=flipud(A);%��������
j=rot90(A);%��������
k=sort(A);%��������


