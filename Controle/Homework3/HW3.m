%% Exercise 1
clear all; clc;

syms s;
num = [1 5 6];
f1 = [1 6];
f2 = [1 2 3];
f3 = [1 9 20];
den = conv(f1,conv(f2,f3));
G = tf(num,den);

rlocus(G)
% axis([-1.7 -1.2 2.6 3.2])    %Eixo para selecionar melhor o ponto zeta=0.45
% axis([-0.01 0.01 6.31 6.35]) %Eixo para selecionar melhor o ponto onde
                               %cruza o eixo imaginario
axis([-10 10 -10 10])
z=0.45; wn=0;
sgrid(z,wn)
[k,p] = rlocfind(G)

%% Exercise2
%2.1 e 2.2
clear all;clc;

G1 = tf(10);

f1 = [1 3 2];
f2 = [1 0 0];
f3 = [1 15 74 120];
G2 = tf(f1,conv(f2,f3));

f4 = [1 6];
f5 = [1 17 72];
H = tf(f4,f5);

T = feedback(G1*G2,H);
G = T /(1-T);
G = minreal(G)
Kp = dcgain(G)

error = 10 / (1 + Kp)

%% Exercise3
clear all;clc;

f1 = [ 1 1]
f2 = [ 1 -2]
f3 = [ 1 3]
den = conv(f1,conv(f2,f3))
G1=tf(1,den)

figure(1);
rlocus(G1)
grid on;

T2 = tf([1 1],[1 10]);
G2 = G1 * T2
figure(2);
rlocus(G2)
grid on;

T3 = tf(conv([1 1],[1 3]),[1 30 225]);
G3 = G1 * T3
figure(3);
rlocus(G3)
grid on;

%% Exercise4
clear all;clc;

G1 = tf(20)

f1 = [ 10 1 ]
f2 = [ 2 1 ]
f3 = [ 0.2 1 ]

G2 = tf(1,conv(f1,conv(f2,f3)))

G = G1*G2

figure(1);
bode(G)
grid on;

figure(2);
nyquist(G)
grid on;

%% Exercise 5
clear all;clc;

S1 = 2 ; S2 = 4; K1 = 3; K2 = 4;
a1 = K1/S1 ; a2 = K2/S2 ; a3 = S2;
numg = [ a1/a3 ]; deng = [ 1 a1+a2 a1*a2];
G = tf( numg, deng)

overshoot = 10;
z=-log(overshoot/100)/sqrt(pi^2+[log(overshoot/100)]^2);
% Plot uncompensated root locus
figure(1);
rlocus(G)
axis([-10 10 -10 10])
% Overlay desired percent OS line
sgrid(z,0)
title(['Uncompensated Root Locus with ', num2str(overshoot),'% OS Line'])

%Generate gain, K, and closed-loop poles, p, for point selected ...
%interactively on the root locus
[K,p]=rlocfind(G)

Tss0 = 4/abs(real(p(1)));

% Simulate uncompensated closed-loop
T=feedback(K*G,1) % Find uncompensated T(s)
[y,t]=step(T); % Step response of uncompensated system

Tssf = Tss0/2;
% Calculate natural frequency
wn=4/(Tssf*z);
% Calculate desired dominant pole location
desired_pole=(-z*wn)+(wn*sqrt(1-z^2)*i);
% Calculate angular contribution to desired pole without PD compensator
angle_at_desired_pole=(180/pi)*...
angle(polyval(numg,desired_pole)/polyval(deng,desired_pole));
% Calculate required angular contribution from PD compensator
PD_angle=180-angle_at_desired_pole;
% Calculate PD zero location
zc=((imag(desired_pole)/tan(PD_angle*pi/180))-real(desired_pole));

% PD Compensator
numc=[1 zc]; % Calculate numerator of Gc(s)
denc=[0 1]; % Calculate denominator of Gc(s)
Gc=tf(numc,denc) % Create and display Gc(s)
Ge=G*Gc % Cascade G(s) and Gc(s)

% Plot compensated root locus
figure(2);
rlocus(Ge)
axis([-10 10 -10 10])
sgrid(z,0) % Overlay desired % OS line
title(['PD Compensated Root Locus with ' , num2str(overshoot),'% OS Line'])

[K,p]=rlocfind(Ge)
Tssprat =4/abs(real(p(1)))

% PD compensated system
Tc=feedback(K*Ge,1) % PD compensated T(s).
[yc,tc]=step(Tc,t); % Step response for PD compensated system.

% Compare
figure(3);
plot(tc,yc,'LineWidth', 1.5); hold on; axis tight
plot(t,y, 'LineWidth', 1.5, 'Color','r'); grid on
legend('Compensated', 'Uncompensated')
title('System response comparison')
set(gca,'FontSize',12)
hold off