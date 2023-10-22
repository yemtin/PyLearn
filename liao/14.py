'''import matplotlib.pyplot as plt
from vector_drawing import *
dino_vectors=[(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),(-5,3),(-5,2),(-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),(-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),(5,1),(6,4)]
def add(v1,v2):
    return(v1[0]+v2[0],v1[1]+v2[1])
dino_vectors2=[add((-1.5,-2.5),v) for v in dino_vectors]
draw(Points(*dino_vectors,color='blue'),Polygon(*dino_vectors,color='blue'),Points(*dino_vectors2,color='red'),Polygon(dino_vectors2,color='red'))
plt.show()'''



'''import matplotlib.pyplot as plt
from vector_drawing import *
points=Points((2,2,red),(-1,3,red))
segment=Segment((2,2,red),(-1,3,red))
draw(points,segment)

plt.show()'''


'''import matplotlib.pyplot as plt

# Define the points and segment
points = [(2, 2), (-1, 3)]
segment = [(2, 2), (-1, 3)]

# Define the colors for each point
point_colors = ['red', 'blue']

# Plot the points and segment
for i, point in enumerate(points):
    plt.scatter(*point, color=point_colors[i])

# Plot the segment
x_values, y_values = zip(*segment)
plt.plot(x_values, y_values, color='green')

plt.show()'''

import matplotlib.pyplot as plt
from vector_drawing import *
dino_vectors=[(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),(-5,3),(-5,2),(-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),(-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),(5,1),(6,4)]
max(dino_vectors,key=length)


