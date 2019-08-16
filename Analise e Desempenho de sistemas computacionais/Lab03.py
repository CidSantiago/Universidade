# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
from sklearn import model_selection
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

names = ["N1","V1","N2","V2","N3","V3","N4","V4","N5","V5","Poker Hand"]
df = pd.read_csv("poker-hand-training-true.data", names=names )
print(df.describe())
print("\n\n")
print(df.head())
print("\n\n")
print(df.tail())

corr = df.corr() #Coeficientes de correlação
print(corr)
pd.plotting.scatter_matrix(df,figsize=(10,10)) #plota todos as matrizes de correlaçao
corr.style.background_gradient(cmap='coolwarm').set_precision(2) #Plota matriz de coeficientes de correlação

array = df.values
X = array[:,0:9]
Y = array[:,10]

seed = 50
scores = []
for i in range(100):
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.20, random_state=seed+i)
    #lm = linear_model.LinearRegression()
    gnb = GaussianNB()
    lda = LinearDiscriminantAnalysis()
    model = gnb.
    model = lda.fit(X_train,Y_train)
    scores.append(model.score(X_test,Y_test))

st.mean(scores)
st.median(scores)
st.stdev(scores)

fig = plt.figure(1, figsize=(10, 10))
ax = fig.add_subplot(111)
bp = ax.boxplot(scores)
