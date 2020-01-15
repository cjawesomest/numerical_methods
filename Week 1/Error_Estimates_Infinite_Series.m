close all; clear all; clc
format long
num_sig_bits=4; % Number of significant bits
x=1.8; % Point of interest
n=0; % Bessel order
eps_s=0.5*10^(2-num_sig_bits) % Stopping criteria
J_true=besselj(n,x) % "True" Bessel function value
eps_a=10*eps_s; % Use this to make sure loop is entered
m=0; % Sets up counter
current_approx=0;
results=[];
eps_t=[];
previous_approx=[];
while (eps_a>eps_s)
% Calculate current term numerator and denominator
numerator=(-1)^m*(0.5*x)^(2*m+n);
denominator=factorial(m)*gamma(m+n+1);
% Calculate new approximation
current_approx=current_approx+numerator/denominator;
eps_t=abs((J_true-current_approx)/J_true)*100;
% Store important values
if m>0
eps_a=abs((current_approx-previous_approx)/current_approx)*100;
results(m+1,4)=eps_a;
end
results(m+1,1)=m+1;
results(m+1,2)=current_approx;
results(m+1,3)=eps_t;
% Store the current approximation into the previous approximation
previous_approx=current_approx;
m=m+1;
end
results