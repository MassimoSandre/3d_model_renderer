import utils
import pygame 

class Object():
    def __init__(self, filename, mult, pos=(10,10,10)) -> None:
        self.pos = pos
        
        self.vectors = []
        self.faces = []
        self.__load_from_file(mult,filename)


    def __load_from_file(self,mult, filename):
        f = open(filename,'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            if line[0] == 'v' and line[1] == ' ':
                t = line[2:].split(' ')
                self.vectors.append([float(t[0])*mult,float(t[1])*mult,float(t[2])*mult])
            elif line[0] == 'f':
                t = line[2:].split(' ')
                
                self.faces.append([int(t[0].split('/')[0]),int(t[1].split('/')[0]),int(t[2].split('/')[0])])
        


    def set_pos(self, pos):
        self.pos = pos

    def rotate_x(self, theta) -> None:
        for i in range(len(self.vectors)):
            self.vectors[i] = utils.rotate_x(self.vectors[i], theta)

    def rotate_y(self, theta) -> None:
        for i in range(len(self.vectors)):
            self.vectors[i] = utils.rotate_y(self.vectors[i], theta)

    def rotate_z(self, theta) -> None:
        for i in range(len(self.vectors)):
            self.vectors[i] = utils.rotate_z(self.vectors[i], theta)

    def render(self,window):
        vertex2d = []
        for v3 in self.vectors:
            vertex2d.append(utils.project_z(utils.vector_sum(v3,self.pos))[:2])

        #print(vertex3d)

        for tri in self.faces:
            cur_tri = []
            for comp in tri:
                cur_tri.append(vertex2d[comp-1])
            pygame.draw.polygon(window, (255,255,255), cur_tri, 1)