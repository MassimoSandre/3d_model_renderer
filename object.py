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

    def render(self,window, projection, camera):
        vertex2d = []
        for v3 in self.vectors:
            vertex2d.append(projection.project(utils.vector_sum(v3,self.pos)))

        #print(vertex3d)

        for tri in self.faces:
            cur_tri = []
            for comp in tri:
                cur_tri.append(self.vectors[comp-1])

            line1 = [0,0,0]
            line2 = [0,0,0]
            line1[0] = cur_tri[1][0] - cur_tri[0][0]
            line1[1] = cur_tri[1][1] - cur_tri[0][1]
            line1[2] = cur_tri[1][2] - cur_tri[0][2]

            line2[0] = cur_tri[2][0] - cur_tri[0][0]
            line2[1] = cur_tri[2][1] - cur_tri[0][1]
            line2[2] = cur_tri[2][2] - cur_tri[0][2]

            

            normal = utils.normalize(utils.cross_product(line1,line2))

            
            t = utils.dot_product(normal,utils.vector_sum(cur_tri[0], self.pos, utils.k_vector(camera,-1)))
            
            if t < 0:
                light = utils.normalize((0,0,-1))
                a = utils.dot_product(light,normal)
                
                color =[128+127*a]*3 #[55+int(200*a)]*3

                cur_tri = []
                for comp in tri:
                    cur_tri.append(vertex2d[comp-1])

                pygame.draw.polygon(window, color, cur_tri, 0)

