"""
IAAC - Master of Computation for Architecture & Design (MaCAD)
Seminar: Digital tools for Algorithmic Geometrical Optimization
Faculty: David Andres Leon, Dai Kandil 
Student: Felipe Romero 
Assignment 02 - Part B Mesh Script

"""


import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import math
import ghpythonlib.components as ghc

#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
#output the vectors to a
mesh = m
sunvec = s
Fnormals = mesh.FaceNormals.ComputeFaceNormals()

a = mesh.FaceNormals   


#2.
#get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
#store the centers into a list called centers 
#output that list to b

centers = []

faces = mesh.Faces.Count

for i in range (faces):
    Fcen = mesh.Faces.GetFaceCenter(i)
    centers.append(Fcen)

b = centers


#3.
#calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
#store the angles in a list called angleList and output it to c


vecCen = rg.Vector3d (Fcen)
angleList = []

for i in range (len(centers)):
    angle = (rg.Vector3d.VectorAngle(vecCen,a[i]))
    angleList.append(angle)



c = angleList

#print(type(angleList))

c = angleList


#4. explode the mesh - convert each face of the mesh into a mesh
#for this, you have to first copy the mesh using rg.Mesh.Duplicate()
#then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
#and store the result into a list called exploded in output d

meshCopy = rg.Mesh.Duplicate(mesh)
facesCopy = meshCopy.Faces.Count
#print(meshCopy.Faces.Count)

exploded = []

for j in range(facesCopy):
    facExt = meshCopy.Faces.ExtractFaces([0])
    exploded.append(facExt)

d = exploded


#after here, your task is to apply a transformation to each face of the mesh
#the transformation should correspond to the angle value that corresponds that face to it... 
#the result should be a mesh that responds to the sun position... its up to you!
