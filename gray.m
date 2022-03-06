path='/Users/xbunax/Downloads/原始数据 前五列是工艺参数，后三列是过滤性能（包括过滤效率、过滤阻力、透气量） 17个样本(1).xls';
gray=xlsread(path);
a,b=size(gray);
for j=2:b
    gray(:,j)=gray(:,j)/gray(2,j);
end

    