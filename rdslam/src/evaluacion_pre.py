#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn import linear_model

c_limit=0
cont = 0
def interpolacion(vec2):
    vec = []
    for intr in vec2:
       vec.append(intr)
    for i in range(len(vec)):
        coord = vec[i]
        vec_inter = [] 
        cont = 0
        if coord[0] == float("inf"): 
           if i != 0:
             vec_inter.append(vec[i-1])
             band = True
             while band:
                if cont+i !=len(vec) and vec[i+cont][0] == float("inf") :
                   vec_inter.append(vec[i+cont])
                else:
                  band=False 
                cont += 1 
             try:   
               vec_inter.append(vec[i+cont-1])   
               vec_inter = interpolar(vec_inter)
             except:
               cont = 2
               vec_inter.append(vec[i-cont]) 
               vec_inter = extrapolacion(vec_inter,0,-1)
             vec_inter2 = np.delete(vec_inter,0,axis=0)
             vec_inter = np.delete(vec_inter2,(len(vec_inter2)-1),axis=0) 
             for j in range(len(vec_inter)):
                     vec[i+j][0] = float(vec_inter[j][0])
                     vec[i+j][1] = float(vec_inter[j][1])
               
           elif i == 0:
             while  vec[i+cont][0] == float("inf"):
                vec_inter.append(vec[i+cont])
                cont += 1
             vec_inter.append(vec[i+cont])
             cont += 1
             while  vec[i+cont][0] == float("inf"):
                cont += 1
             vec_inter.append(vec[i+cont])
             vec_inter = extrapolacion(vec_inter,-2,-1)
             vec_inter2 = np.delete(vec_inter,(len(vec_inter)-1),axis=0)
             vec_inter = np.delete(vec_inter2,(len(vec_inter2)-1),axis=0) 
             for j in range(len(vec_inter)):
                     vec[i+j][0] = float(vec_inter[j][0])
                     vec[i+j][1] = float(vec_inter[j][1])       
        else:
           vec[i][0] = float(vec[i][0])
           vec[i][1] = float(vec[i][1])
    return(vec)

def interpolar(vec_inter):
    y1,x1 = vec_inter[0]
    y2,x2 = vec_inter[-1]
    y_pred, A, B = regresion_lineal([[float(x1)],[float(x2)]], [float(y1),float(y2)])
    for i in range(len(vec_inter)):
       if vec_inter[i][0] == float("inf"):
          vec_inter[i][0] = float(ecuacion(A,B,float(vec_inter[i][1])))
    return(vec_inter)
       
def extrapolacion(vec_inter,a,b):
    y1,x1 = vec_inter[a]
    y2,x2 = vec_inter[b]
    y_pred, A, B = regresion_lineal([[float(x1)],[float(x2)]], [float(y1),float(y2)])
    for i in range(len(vec_inter)):
       if vec_inter[i][0] == float("inf"):
          vec_inter[i][0] = float(ecuacion(A,B,float(vec_inter[i][1])))
    return(vec_inter)
    
def regresion_lineal(X_train, y_train):
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_train) 
    return(y_pred,regr.coef_,regr.intercept_)
    
def ecuacion(A,B,x):#en esta ecuación se obtiene  
    y= (A*x)+B 
    return(y)
            




