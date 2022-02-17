import math
from optparse import TitledHelpFormatter
import re

def k_vector(vec, k):
    result = []
    for i in vec:
        result.append(i*k)
    return tuple(result)

def vector_sum(vec1, vec2, *argv):
    result = [0,0,0]

    for i in range(len(vec1)):
        result[i] = vec1[i]+vec2[i]
        for arg in argv:
            result[i]+=arg[i]

    return tuple(result)

def normalize(vec):
    l = math.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    if l == 0:
        return vec
    return k_vector(vec, 1/l)

def cross_product(vec1, vec2):
    x = vec1[1]*vec2[2] - vec1[2]*vec2[1]
    y = vec1[2]*vec2[0] - vec1[0]*vec2[2]
    z = vec1[0]*vec2[1] - vec1[1]*vec2[0]
    return (x,y,z)

def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        return None
    result = 0
    for i in range(len(vec1)):
        result += vec1[i]*vec2[i]
    return result

def matrix_vector_product(mat, vec):
    if len(mat) != len(vec):
        return None
    result = []
    for line in mat:
        result.append(dot_product(line, vec))

    return tuple(result)

def rotate_x(vec, theta):
    mat = [(1, 0,0), (0, math.cos(theta), -math.sin(theta)), (0, math.sin(theta), math.cos(theta))]

    return matrix_vector_product(mat, vec)

def rotate_y(vec, theta):
    mat = [(math.cos(theta), 0, math.sin(theta)), (0,1,0) , (-math.sin(theta), 0, math.cos(theta))]

    return matrix_vector_product(mat, vec)

def rotate_z(vec, theta):
    mat = [(math.cos(theta), -math.sin(theta),0), (math.sin(theta), math.cos(theta),0), (0,0,1)]

    return matrix_vector_product(mat, vec)
    
class Projection():
    def __init__(self,fov,screen_size) -> None:
        self.NEAR = 0.1
        self.FAR = 1000
        self.fov = fov
        self.screen_size = screen_size
        self.aspect_ratio = screen_size[1]/screen_size[0]

    def project(self, vec):
        x = self.aspect_ratio*(1/math.tan(self.fov/2))*vec[0]/vec[2]
        y = (1/math.tan(self.fov/2))*vec[1]/vec[2]

        x+=1
        y+=1
        x*= 0.5*self.screen_size[0]
        y*= 0.5*self.screen_size[1]

        return (x,y)
        

# def project_z(vec):
#     base = [(1,0,0), (0,1,0)]

#     result = (0,0,0)
#     for b in base:
#         p = dot_product(vec, b)
#         result = vector_sum(result,k_vector(b, p))
    
#     return result

