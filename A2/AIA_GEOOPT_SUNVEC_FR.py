"""
IAAC - Master of Computation for Architecture & Design (MaCAD)
Seminar: Digital tools for Algorithmic Geometrical Optimization
Faculty: David Andres Leon, Dai Kandil 
Student: Felipe Romero 
Assignment 02 - Part A Sun Vector Script

"""

import Rhino.Geometry as rg
#import Rhinoscriptsyntax as rs
import math 

#create a sun vector

#1. create a Sphere at point (0,0,0) with radius 1 and output it to a
#output the sphere to a
#center = rg.Point3d(0,0,0)

center = rg.Point3d(0,0,0)
sphere = rg.Sphere(center, radius=1)
a = sphere

#2. evaluate a point in the sphere using rg.Sphere.PointAt() at coordintes x and y
#the point should only be on the upper half of the sphere (upper hemisphere)
#the angles are in radians, so you might want to use math.pi for this
#output the point to b -

lon = (x/math.pi)*360 # NOT WORKING PROPERLY
lat = y*math.pi
point = rg.Sphere.PointAt(a, lon, lat)

b = point


#create a vector from the origin  and reverse the vector
#keep in mind that Reverse affects the original vector
#output the vector to c

vec1 = rg.Vector3d (b)
#vec2 = rg.Vector3d (center)

vecdir = rg.Line(center,b)
vecneg = rg.Vector3d.Reverse(vec1)

c = vecneg
d = vecdir
