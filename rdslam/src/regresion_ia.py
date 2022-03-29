#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib
import rospy
import sys
import cv2
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import os
import math
import numpy as np
import pandas as pd
import seaborn as sb
import os
import statistics 
import scipy as sp
from scipy.signal.signaltools import correlate2d as c2d 

def deteccion_dinamico(matriz1, cont_sec, carpeta, zona_ant, thres):
  data_m = pd.DataFrame(matriz1, columns=['r', 'dr', 'alfa'])
  data_seg, zona, umb, thres_bool = segmenta_max(data_m, zona_ant, thres)
  if thres_bool:
    data_zona = segmenta_zonas(data_m, umb)
    data_m = pd.DataFrame(data_zona, columns=['r', 'dr', 'alfa','n','seg','color'])
    data = []
    bolsa_front = []
    band = True
    capa = min(data_m['seg'].values)
    top_c = max(data_m['seg'].values)+1
    while band:# determinamos las diferentes zonas que tiene con negativo alta variabilidad positivo zonas baja variabilidad
         datos_s = data_m[(data_m['seg'] == capa) & (data_m['dr'] > 0)]
         if len(datos_s) != 0:
            n_dat = datos_s['n'].values
            max_dat = max(n_dat)
            min_dat = min(n_dat)
            clas = 0
            if capa<0:
               clas = -1
            if capa !=0:
               bolsa_front.append([max_dat, min_dat, max_dat-min_dat, clas])
            data.append(datos_s)
         capa += 1
         if capa == 0:
           capa += 1
         if capa >= top_c:
            band = False
    if len(zona) != 0:
       dr_p = umbral_move(bolsa_front)#se establece cuanto fue lo maximo que se pudo mover una zona 
       bolsa_front, band_end,zona = detectar_dinamico(bolsa_front, zona, dr_p)
       if band_end:
          max_ant = zona_ant[0]+zona_ant[3]
          min_ant = zona_ant[1]-zona_ant[3]
          if max_ant > 90:
            max_ant = 90
          if min_ant < 0:
             min_ant = 0                  
          zona = [max_ant, min_ant, max_ant-min_ant,zona_ant[3]]
       if carpeta != None:
          data = []
          data.append(data_m[(data_m['seg'] == 0)])  
       return(zona)
    else:
       return([0, 90, 0,0])
  else:     
       return(zona)

def umbral_move(bolsa_in):
    max_long = 0
    for i in range(len(bolsa_in)):
      if bolsa_in[i][3] <0 and bolsa_in[i][2] > max_long:
         max_long =  bolsa_in[i][2]    
    return(max_long)       
        
def detectar_dinamico(bolsa_in, zona, dr_p):
    ''' debo mejorar el criterio para seleccionar la zona dinámica puede ser la correlación'''
    max_vect = []
    for elem in bolsa_in:#ordena la bolsa de menor a mayor de este modo se ordenan los espacios 
       max_vect.append(elem[0])
    max_vect = list(max_vect)
    max_vect.sort()   
    vect_ord = []
    for n_ord in max_vect:
       for bol in bolsa_in:
         if bol[0] == n_ord:
            vect_ord.append(bol)
    cont_alt = 0
    band_enc = False
    for i in range(len(vect_ord)):
       if vect_ord[i][3] <0 and cont_alt == 0:
          cont_alt = 1 
          try:    
             max_det, min_det, long_det = vect_ord[i+1][0],vect_ord[i][1],vect_ord[i+1][2]
          except:
             try:
                max_det, min_det, long_det, zn = zona
             except:
                max_det, min_det, long_det = zona
       elif vect_ord[i][3] <0 and cont_alt == 1 and vect_ord[i-1][3] == 0:
          vect_ord[i-1][3] = 1
          cont_alt = 1
          max_det = vect_ord[i][0]
          band_enc = True
    zona =  [max_det, min_det, long_det, dr_p]
    
    return(vect_ord, not(band_enc),zona)    

def segmenta_max(matriz, zona, thres):
   dr_eva = []
   cont = 1
   n = 1
   band = True
   dr_v = matriz['dr'].values
   if thres<max(dr_v):
    umb=max(dr_v)/2
    for i in range(len(matriz)):
       r = matriz['r'][i]
       dr = matriz['dr'][i]
       alf  = matriz['alfa'][i]
       if dr > umb:
          dr_eva.append((r,dr,alf,i))
    dr_eva = np.array(dr_eva) 
    dr_f_seg = []
    if len(dr_eva) >1  : 
       not_e = 0  
       for l in range(len(dr_eva)-1):
             n  = dr_eva[l][3]
             n_1  = dr_eva[l+1][3]
             if abs(n_1-n) == 1:
                if dr_eva[l][1] < dr_eva[l+1][1]:
                   dr_f_seg.append(dr_eva[l+1])
                else:
                   dr_f_seg.append(dr_eva[l])
                   dr_eva[l+1] = dr_eva[l]
             else:
                dr_f_seg.append(dr_eva[l])
       n  = dr_eva[len(dr_eva)-1][3]
       n_1  = dr_eva[len(dr_eva)-2][3]
       if abs(n_1-n) == 1:
          if dr_eva[len(dr_eva)-1][1] > dr_eva[len(dr_eva)-2][1]:
             dr_f_seg[len(dr_f_seg)-1] = dr_eva[len(dr_eva)-1]
       else:
          dr_f_seg.append(dr_eva[len(dr_eva)-1])        
       dr_eva = dr_f_seg  
       dr_f_seg = []
       dr_f_seg.append(dr_eva[0])
       for o in range(len(dr_eva)-1):
          if dr_eva[o][3] != dr_eva[o+1][3]:
             dr_f_seg.append(dr_eva[o+1])       
       dr_eva = dr_f_seg  
    dr_eva = np.array(dr_eva)  
       
    for j in range(len(dr_eva)-2):
       dr_v = dr_eva[:,1] 
       dr_v_min = min(dr_v)
       for k in range(len(dr_eva)):
          if dr_eva[k][1] == dr_v_min:
             dr_eva = np.delete(dr_eva,k, axis=0) 
             break       
    dr_v = dr_eva[:,1] 
    if len(dr_v) == 2:       
       max_dr = max(dr_v)
       min_dr = min(dr_v)
    else:
       max_dr = dr_v
       min_dr = dr_v
    matriz_seg = []
    min_n, max_n = 0,0   
    
    for i in range(len(matriz)):
       r = matriz['r'][i]
       dr = matriz['dr'][i]
       alf  = matriz['alfa'][i]
       if dr == max_dr:
          col = [0,255,0]
          matriz_seg.append([r,dr,alf,i,col])
          max_n = i
       elif dr == min_dr: 
          col = [0,255,0]
          matriz_seg.append([r,dr,alf,i,col])
          min_n = i 
       else:
          col = [0,0,255]
          matriz_seg.append([r,dr,alf,i,col])
    if  min_dr == max_dr and len(zona)>0:
        if abs(max_n-zona[0]) < abs(max_n-zona[1]):
          if max_n-zona[2] < 0:
             min_n = max_n-zona[2]
          else:
             min_n = 0 
          if min_n<0:
             min_n = 0
          matriz_seg[min_n][4] = [0,255,0]
        else:
          min_n = max_n
          max_n = min_n+zona[2]
          if max_n > 89:
             matriz_seg[89][4] = [0,255,0] 
          else:   
             matriz_seg[max_n][4] = [0,255,0]  
    vect = [max_n, min_n] 
    max_n = max(vect)
    min_n = min(vect)  
    if len(zona) == 4:  
       max_a,min_a,long_a,dp = zona
       if abs(max_a-max_n) > abs(min_a-max_n):
           min_n_p = min_n
           min_n = max_n
           max_n = min_n_p   
       if abs(max_n-max_a)>abs(min_a-min_n):
          if abs(min_n-max_n) > abs(long_a+dp):
             max_n = min_n+long_a+dp 
       else:
          if abs(min_n-max_n) > abs(long_a+dp):
             min_n = max_n+long_a+dp  
             
       if max_n-min_n < 0:
          if abs(max_a-max_n) < abs(min_a-min_n):
             min_n = max_a-long_a
          else:
             max_n = min_n+long_a 
    zona = [max_n, min_n, max_n-min_n]
    return(matriz_seg, zona,umb, True)
   else:
     zona = [0, 90, 0,0]
     return( matriz, zona, 0, False)
def segmenta_zonas(matriz, umb):# se divide en zonas a partir de la superación del umbral dinámico
    segmen = []
    cont = 1
    cont_0 = -1
    n = 1
    band = True
    band_0 = True
    np_matriz = np.array(matriz)
    for ele in np_matriz:
       r,dr,alf = ele 
       if dr > umb:
          band_0 = True
          if band:
             cont += 1
             band = False
          col = [0,150,155]
          segmen.append([r,dr,alf,n ,cont_0,col])
       else:  
          segmen.append([r,dr,alf,n ,cont,color(cont)])
          band = True
          if band_0:
             cont_0 -= 1
             band_0 = False
       n += 1 
    return(segmen)
         
def color(num):
    c = (num) * 130
    if c<255:
       col = [c,0,0]
    elif c<510 and c>=255:
       c = c-255
       col = [255,c,0]   
    elif c>=510 and c<765:
       c = c-510
       col = [255,255,c]
    else:
       col = [255,255,255]  
    return(col)       




    
    
    
    
    
    
