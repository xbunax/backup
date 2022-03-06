function [fitresult, gof] = createFit(v, z)
%CREATEFIT(V,Z)
%  Create a fit.
%
%  Data for 'untitled fit 1' fit:
%      X Input : v
%      Y Output: z
%  Output:
%      fitresult : a fit object representing the fit.
%      gof : structure with goodness-of fit info.
%
%  另请参阅 FIT, CFIT, SFIT.

%  由 MATLAB 于 28-Jul-2019 20:01:42 自动生成


%% Fit: 'untitled fit 1'.
[xData, yData] = prepareCurveData( v, z );

% Set up fittype and options.
ft = fittype( 'smoothingspline' );

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, 'Normalize', 'on' );

% Plot fit with data.
figure( 'Name', 'untitled fit 1' );
h = plot( fitresult, xData, yData );
legend( h, 'z vs. v', 'untitled fit 1', 'Location', 'NorthEast' );
% Label axes
xlabel v
ylabel z
grid on


