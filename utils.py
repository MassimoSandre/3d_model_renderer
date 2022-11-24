import math
from optparse import TitledHelpFormatter

def k_vector(vec, k):
    result = []
    for i in vec:
        result.append(i*k)
    return result

def length(vec):
    t = 0
    for i in vec:
        t += i**2
    return math.sqrt(t)

def normalize(vec):
    l = length(vec)
    return k_vector(vec,1/l)

def vector_sum(vec1, vec2, *argv):
    result = [0]*len(vec1)

    for i in range(len(vec1)):
        result[i] = vec1[i]+vec2[i]
        for arg in argv:
            result[i]+=arg[i]

    return result

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

    return result

def rotate_x(vec, theta):
    mat = [(1, 0,0), (0, math.cos(theta), -math.sin(theta)), (0, math.sin(theta), math.cos(theta))]

    return matrix_vector_product(mat, vec)

def rotate_y(vec, theta):
    mat = [(math.cos(theta), 0, math.sin(theta)), (0,1,0) , (-math.sin(theta), 0, math.cos(theta))]

    return matrix_vector_product(mat, vec)

def rotate_z(vec, theta):
    mat = [(math.cos(theta), -math.sin(theta),0), (math.sin(theta), math.cos(theta),0), (0,0,1)]

    return matrix_vector_product(mat, vec)
    

def project(vec, aspect_ratio, fov=90 ):
    f = 1000.0
    n = 0.1
    ffov = 1/math.tan(fov*0.5*math.pi/180)
    
    mat = [[0 for _ in range (4)] for _ in range(4)]
    mat[0][0] = aspect_ratio * ffov;
    mat[1][1] = ffov;
    mat[2][2] = f / (f - n);
    mat[2][3] = (-f * n) / (f - n);
    mat[3][2] = 1.0;
    mat[3][3] = 0.0;
    
    result = matrix_vector_product(mat, (*vec,0))
    
    if result[-1] != 0:
        return k_vector(result[:2], 1/result[-1])
    return result[:2]

