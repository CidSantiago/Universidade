function [dxdt] = myode(t,x,ut,u)
%MYODE Summary of this function goes here
%   Detailed explanation goes here

u = interp1(ut,u,t); % Interpolate the data set (ut,u) at time t
dxdt = x^2-u*x-2*u; % Evaluate ODE at time t
end

