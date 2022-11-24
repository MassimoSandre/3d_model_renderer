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
    
    def __get_color(self,r):
        return [int(255*r)]*3

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

    def render(self,window,camera,light_direction):
        def f(e):
            return (self.vectors[e[0]-1][2] + self.vectors[e[1]-1][2] + self.vectors[e[2]-1][2])/3
        self.faces.sort(key=f,reverse=True)
        screen_height = window.get_rect().height
        screen_width = window.get_rect().width
        aspect_ratio = screen_height/screen_width

        tv = []
        for v in range(len(self.vectors)):
            tv.append(utils.vector_sum(self.vectors[v],(0,0,6)))

        for tri in self.faces:
            cur_tri = []
            v1 = tv[tri[1]-1][0] - tv[tri[0]-1][0], tv[tri[1]-1][1] - tv[tri[0]-1][1], tv[tri[1]-1][2] - tv[tri[0]-1][2] 
            v2 = tv[tri[2]-1][0] - tv[tri[0]-1][0], tv[tri[2]-1][1] - tv[tri[0]-1][1], tv[tri[2]-1][2] - tv[tri[0]-1][2] 

            normal = v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0]
            normal = utils.normalize(normal)

            c = normal[0]*(tv[tri[0]-1][0]-camera[0]) + normal[1]*(tv[tri[0]-1][1]-camera[1]) + normal[2]*(tv[tri[0]-1][2]-camera[2])

            if c < 0:
                for comp in tri:
                    cur_vertex = utils.project(tv[comp-1],aspect_ratio)
                    cur_vertex = utils.vector_sum(cur_vertex, (1,1))
                    cur_vertex[0] *= screen_width/2
                    cur_vertex[1] *= screen_height/2
                    cur_tri.append(cur_vertex)

                r = utils.dot_product(normal,light_direction)
                pygame.draw.polygon(window, self.__get_color(r), cur_tri)