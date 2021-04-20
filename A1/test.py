import Rhino.Geometry as rg

grid = []

for i in range(2):
    for j in range(12):
        grid.append(rg.Point3d(i,j,0))


a = grid

line = rg.Line(grid[0], grid[18])



b = line.Length
