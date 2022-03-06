n = 6;
a = cell(1,n);
for j = 1:n
  a{j} = linspace(0, 1, 2^j);
end
m = n;
for j = 1:n
  b = a{j};
  l = ones(1, length(b)) * m;
  plot(b, l, 'ro-'), hold on
  m = m - 1;
end
xlim([-0.1 1.1]), ylim([0 n+1])