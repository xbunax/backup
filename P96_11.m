clc;
clear;
A=magic(3);
a=triu(A);%整个矩阵
b=tril(A);%整个矩阵
c=[sum(A(1,:)) sum(A(2,:)) sum(A(3,:))];%整行
d=[sum(A(:,1)) sum(A(:,2)) sum(A(:,3))];%整列
e=median(A);%单个元素
f=diag(A);%整个矩阵
g=A';%整个矩阵
h=fliplr(A);%整个矩阵
i=flipud(A);%整个矩阵
j=rot90(A);%整个矩阵
k=sort(A);%整个矩阵


