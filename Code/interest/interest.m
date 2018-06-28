%% Simple Interest
I = 0;          %Interest Earned
P = 10000;      %Principal
r = 0.03;       %Interest Rate (decimal) 
t = 3;          %Term (years)

format bank
I = P*r*t

%% Compound Interest
A = 0;         %Future Value
P = 385000;    %Principal
r = 0.06;      %Interest Rate (decimal)
n = 12;        %Number of times compouned in 1 't'
t = 1;         %Term (years)

format bank
disp("Total After Investment")
A = P*(1+(r/n))^(n*t)
disp("Return on Investment")
B = A - P
%% Loan Repayment/ Installment
A = 0;          %Installment
P = 31000;      %Principal
r = 0.28;       %Interest rate per period
n = 50;         %Total number of payments or periods
format bank

J = r/12;       %Effective interest rate
A = P *( J/ (1-(1+J)^-n ))

%% Amortization Schedule

A = 0;          %Future Value
r = 0.12;       %Interest Rate (decimal)
n = 12;         %Number of times compouned in 1 't'
t = 20;         %Term (years)

format bank
Rate = r/n;
NumPeriods =  t*12;
presentVal = 100000;

[Principal, Interest, Balance, Payment] = amortize(Rate, NumPeriods, presentVal );

plot(Balance,'b'), hold('on')
plot(cumsum(Principal),'--k')
plot(cumsum(Interest),':r')

xlabel('Payment Month')
ylabel('Rand')
grid('on')
title('Outstanding Balance, Cumulative Principal & Interest')
legend('Outstanding Balance', 'Cumulative Principal', ... 
'Cumulative Interest')