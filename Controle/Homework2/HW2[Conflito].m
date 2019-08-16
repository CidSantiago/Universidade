%%Exercise 1%%

[Xa,Ya] = textread('HW2_ex1_dataA.txt','%f %f');
[Xb,Yb] = textread('HW2_ex1_dataB.txt','%f %f');

syms s
a = 0.2376;
ka = 2.5543;
numa = ka
dena = [ 1 a]
Ga = tf(numa,dena)
figure(3)
step(Ga);  hold on;
plot(Xa,Ya,'color','r')

figure(2)
plot(Xb,Yb)
grid on