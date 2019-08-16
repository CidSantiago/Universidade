%Exercise 1.1
syms s
F1(s) = (s - 10)/((s+2)*(s+5))
ilaplace(F1)

%Exercise 1.2
syms s
F2(s) = 100 /((s+1)*(s^2+ 4*s + 13))
ilaplace(F2)

%Exercise 1.3
syms s
F3(s) = (s+18) / (s*((s+3)^2))
ilaplace(F3)

%Exercise 2.1
%Degrau
syms s
Y1(s)= (s+10)/(s*(s+4)*(s+8))
ilaplace(Y1)

num=[1 10];
den=[1 12 32];
G=tf(num,den);
step(G)

%Impulso
syms s
Y2(s)= (s+10)/((s+4)*(s+8))
ilaplace(Y2)

num=[1 10];
den=[1 12 32];
G=tf(num,den);
impulse(G)

%Exercise 2.2
%degrau
a = [-4 -2 -1 0 1 2 4]
for i=1:7
    num=[a(i) 10];
    den=[1 12 32];
    G(i)=tf(num,den);
end
step(G)

%impulso
a = [-4 -2 -1 0 1 2 4]
for i=1:7
    num=[a(i) 10];
    den=[1 12 32];
    G(i)=tf(num,den);
end
impulse(G)

%Exercise3.2a
A = [(-3/2) 0;(3/2) (-4/4)];
B=[1; 0];
C=[0 (1/4)];
D=0;

[num,den] = ss2tf(A,B,C,D);
T = tf(num,den)
opt = stepDataOptions('StepAmplitude',2);
step(T,opt)

%Exercise3.2b
A = [(-3/2) 0;(3/2) (-4/4)];
B=[1; 0];
C=[0 (1/4)];
D=0;

[num,den] = ss2tf(A,B,C,D);
T = tf(num,den)
[u,t] = gensig('square',5,30,0.1)
[y,t]=lsim(T,u,t);
figure; plot(t,y)

%Exercise4.3

num=[1 4 4];
den=[4 7 3];
T=tf(num,den);
Tss=ss(T)

A = [0 1;(-7/4) (-3/4)];
B=[0; 1/4];
C=[(13/4) (9/4)];
D=(1/4);

[num,den] = ss2tf(A,B,C,D)
T = tf(num,den)
