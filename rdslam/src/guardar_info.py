#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
import os
                 
       
def guardar_tiempos_client(pos,cont):
      direc = '/home/mab/datos_pcl/datos/guardar_tiempos_client.txt'
      if cont<10:
         if os.path.isfile(direc):
            os.remove(direc)
         enc = "n lapse t_estadistica t_reduccion t_proyeccion t_guardar vx_m  ang_min ang_max ang_delta ang_long x_pos_orb y_pos_orb z_pos_orb rot_x_orb rot_y_orb rot_z_orb puntos_org puntos_reduc"
         archi1=open(direc,"w")  
         archi1.write(enc) 
      archi1=open(direc,"a") 
      archi1.write('\n' + str(int(cont-9))+" "+pos)
      
def guardar_tiempos_reconstruccion(pos,cont):
      direc = '/home/mab/datos_pcl/datos/guardar_tiempos_reconstruccion.txt'
      if cont<10:
         if os.path.isfile(direc):
            os.remove(direc)
         enc = "cont evento lapse t_preparacion t_segmentacion t_concatenacion t_reduccion t_guardar_.ply t_proyeccion_reconstruccion t_proyeccion_dinamico PCL_in PCL_SEG1 PCL_DIN1 PCL_SEG2 PCL_DIN2 PCL_ant PCL_uni PCL_red voxel x_pos_din y_pos_din z_pos_din"
         archi1=open(direc,"w")  
         archi1.write(enc) 
      archi1=open(direc,"a") 
      archi1.write('\n' + str(int(cont-9))+" "+pos)

def guardar_tiempos_reconstruccion_two(pos,cont):
      direc = '/home/mab/datos_pcl/datos/guardar_tiempos_reconstrucciontwo.txt'
      if cont<10:
         if os.path.isfile(direc):
            os.remove(direc)
         enc = "cont lapse t_preparacion t_concatenacion t_reduccion t_guardar_.ply t_proyeccion_reconstruccion PCL_in PCL_ant PCL_uni PCL_red"
         archi1=open(direc,"w")  
         archi1.write(enc) 
      archi1=open(direc,"a") 
      archi1.write('\n' + str(int(cont-9))+" "+pos)



