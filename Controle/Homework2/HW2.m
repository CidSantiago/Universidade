%% Exercise 1
Clear all; clc;

[Xa,Ya] = textread('HW2_ex1_dataA.txt','%f %f');
[Xb,Yb] = textread('HW2_ex1_dataB.txt','%f %f');

%% 1.1 
figure(1);
plot(Xa,Ya)
grid on
title('Sistema A')

figure(2);
plot(Xb,Yb)
grid on
title('Sistema B')

%% 1.3
a = 4/Xa(86)
k = a*Ya(196)
numa = [ k ]
dena = [ 1 a]
Ga = tf(numa,dena)
figure(3)
step(Ga); hold on;
plot(Xa,Ya,'color','r')
grid on;
legend('Estimativa A','Sistema A','Location','southeast')

OS = (max(Yb)-Yb(127))/Yb(127)*100
damp = -log(OS/100)/sqrt((log(OS/100)^2)+pi^2)
wn = pi/(Xb(11)*sqrt(1-damp^2))
numb = [ wn^2 ]
denb = [ 1 2*damp*wn wn^2]
Gb = tf(numb, denb)
figure(4)
step(Gb); hold on;
plot(Xb,Yb,'color','r')
legend('Estimativa A','Sistema A','Location','southeast')

%% Exercise 2

clear all; clc;
s = tf('s');
G1= 1/(s+7); G2= 1/(s^2+2*s+3);
G3= 1/(s+4); G4= 1/s;
G5= 5/(s+7); G6= 1/(s^2+5*s+10);
G7= 3/(s+2); G8= 1/(s+6);

Gm = (G1*G5)/(1+G1*(G2+G3*G5*(G4+G6*G7)+G5*G8))

Sum1 = sumblk('b = r - a - d');
Sum2 = sumblk('d = f + g');
Sum3 = sumblk('h = i + j');

G1.u = 'b'; G1.y = 'e';
G2.u = 'e'; G2.y = 'f';
G3.u = 'h'; G3.y = 'g';
G4.u = 'c'; G4.y = 'i';
G5.u = 'e'; G5.y = 'c';
G6.u = 'c'; G6.y = 'k';
G7.u = 'k'; G7.y = 'j';
G8.u = 'c'; G8.y = 'a';

Ss = connect(G1,G2,G3,G4,G5,G6,G7,G8,Sum1,Sum2,Sum3,'r','c');

[num, den] = ss2tf(Ss.A,Ss.B,Ss.C,Ss.D);
Gs = tf(num,den)
figure(1)
step(Gs,'r',Gm,'b'); grid on;
legend('Simulado','Manual');

%% Exercise 3

clear all; clc;

A = [0 1 0; 0 0 1; -3 -4 -5];
B = [0; 0; 1];
C = [0 1 1];
D = 0;

[num, den] = ss2tf(A,B,C,D);
T = tf(num,den);
G = feedback(T,1);

den = G.den;
s3 = [1 5 0];
s2 = [6 3 0];
s1 = [-det([s3(1) s3(2);s2(1) s2(2)])/s2(1) ...
      -det([s3(1) s3(3);s2(1) s3(3)])/s2(2) 0];
s0 = [-det([s2(1) s2(2);s1(1) s1(2)])/s1(1) ...
      -det([s2(1) s2(3);s1(1) s1(3)])/s1(2) 0];
s0(isnan(s0))=0;
R = [s3(1) s2(1) s1(1) s0(1)]

%% Exercise 4

clear all;clc;

% Item 2
num1=[3 -57];
den1=[1 -3];
temp= tf(num1,den1);
tf1 = feedback(temp,1)
pole1 = pole(tf1)

num2=[3 6];
den2=[1 3];
temp=tf(num2,den2);
tf2 = feedback(temp,1)
pole2 = pole(tf2)

% Item 3
t = 0:0.1:5;
A = 0.1;
input = A*cos(2*t);

[y1,t]=lsim(tf1,input,t);
[y2,t]=lsim(tf2,input,t);

plot(t,y1,'r',t,y2,'b')

ut = linspace(0,10,80);
u = A*cos(2*ut);
tspan = [0 10];
[t,x] = ode45(@(t,x) myode(t,x,ut,u),tspan,0);


