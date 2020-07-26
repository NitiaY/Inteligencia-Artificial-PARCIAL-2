# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:21:15 2020

@author: Usuario
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
Alumno =pd.read_csv('Alumno.csv',header=0)
print(Alumno)
Alumno_Train=pd.read_csv('Alumno_Train.csv',header=0)
print(Alumno_Train)
#------------------Preprocesamiento-----------

Alumno=Alumno.drop(['NOMBRE COMPLETO', 'CI'],axis=1)
Alumno_Train=Alumno_Train.drop(['NOMBRE COMPLETO', 'CI'],axis=1)

Alumno['SEXO'].replace(['F','M'],[0,1],inplace=True)
Alumno_Train['SEXO'].replace(['F','M'],[0,1],inplace=True)
Alumno['DEPARTAMENTO'].replace(['La Paz','Oruro','Cochabamba','Tarija','Beni','Chuquisaca'],[0,1,2,3,4,5],inplace=True)
Alumno_Train['DEPARTAMENTO'].replace(['La Paz','Oruro','Cochabamba','Tarija','Beni','Chuquisaca'],[0,1,2,3,4,5],inplace=True)
Alumno_Train['OBSERVACION'].replace(['reprobado','aprobado'],[0,1],inplace=True)
#print(Alumno)
#print(Alumno_Train)
#----------------PIPELINE----------------------
from sklearn.model_selection import train_test_split
X = np.array(Alumno_Train.drop(['OBSERVACION'],1))
Y = np.array(Alumno_Train['OBSERVACION'])

X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=0.2)

#predicción
modelo = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
modelo.fit(X_train, Y_train)
print("-------prediccion------------")
print(modelo.predict(X_test))

#_------------------otra forma-------------------
from sklearn.tree import DecisionTreeClassifier
model = make_pipeline(StandardScaler(),DecisionTreeClassifier())
model.fit(X_train, Y_train)
print("logistic regression score: %f" % model.score(X_test, Y_test))
print(model.predict(X_test))


