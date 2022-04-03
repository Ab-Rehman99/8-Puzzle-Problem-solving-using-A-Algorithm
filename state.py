
class State:

    def __init__(self,A_star_value,matrix,level): # constructor 
        
        self.matrix = matrix
        self.level = level
        self.A_star_value = A_star_value

    def child_creation(self):
        #locate "*" blanks
        x,y = self.locate_bLANKS(self.matrix,'*')
    
        posi_l = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        list_child = []
        for position in posi_l:
            child = self.swapp(self.matrix,x,y,position[0],position[1]) # swaping the blanks make childs
            if child:
                list_child.append(State(0,child,self.level+1))
        return list_child


    def locate_bLANKS(self,MAT,blank):
        for i, x in enumerate(MAT):
            if blank in x:
                return i, x.index(blank)    

    def swapp(self,puz,x1,y1,x2,y2):
       
        if x2 >= 0 and x2 < 3 and y2 >= 0 and y2 < 3:
            child_matrix = []
            child_matrix = self.copy_mat(puz)
            #swap basic logic
            copied = child_matrix[x2][y2]
            child_matrix[x2][y2] = child_matrix[x1][y1]
            child_matrix[x1][y1] = copied
            return child_matrix
        else:
            return None
            

    def copy_mat(self,mat):
        copied = []
        for rows in mat:
            t = []
            for cols in rows:
                t.append(cols)
            copied.append(t)
        return copied    
            
    

