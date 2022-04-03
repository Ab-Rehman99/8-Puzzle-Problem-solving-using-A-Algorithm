from state import State

class game:

    def __init__(self,size):
       
        self.n = size
        self.open = []
        self.closed = []

    def take_matrix(self):
        mat = []
        for rows in range(self.n):
            row = input().split(" ")

            mat.append(row)
        return mat

        
    def check_if_end(self,current,g):
        if self.hueristic(current.matrix,g) == 0:
            return True
        else:
            return False

    def hueristic(self,initial,end):
       
        cnt = 0
        for rows in range(self.n):
            for colds in range(self.n):
                if initial[rows][colds] != end[rows][colds] and initial[rows][colds] != '*':
                    cnt =cnt+ 1
        return cnt

    def A_star_finder(self,initial,end):
       
        return initial.level+self.hueristic(initial.matrix,end)

    def solve(self,initial,end):
        
        initial:State = State(0,initial,0)
        hueristic=self.A_star_finder(initial,end)  # find hueristic of starting node
        initial.A_star_value = hueristic
        # append the starting node in list
        self.open.append(initial)
        print("\n\n")
        while True:
            cur:State = self.open[0]
            
            print("---------------")
            
            
            #printing the matrix
            for rowws in cur.matrix:
                for cols in rowws:
                    print(cols,end=" ")
                print("\n")
            # check if goal state has been reached or not
            c= self.check_if_end(cur,end)
            if(c == True):
                break
            # append children state into open List:
            for childs in cur.child_creation():
                childs.A_star_value = self.A_star_finder(childs,end)
                self.open.append(childs)
            # putting explored state in closed list: 
            self.closed.append(cur)
            del self.open[0]

            #sort the list according to least Astar value 
           
            self.open.sort(key = lambda x:x.A_star_value,reverse=False)

if __name__ == "__main__":

    choice=int(input("\nDo you want to enter:\n\n 1) Your own Strt and end state.\n\n 2)Use built in initial and end state\n\n"))

    if choice == 1:
        p=game(3)
        print("Enter initial state: \n")
        strt=p.take_matrix()
        print("Enter the Goal matrix: \n")        
        end = p.take_matrix()
        p.solve(strt,end)

    elif choice == 2:

        initial= [ [ 2, 8, 3 ],   
                 [ 1, 6, 4 ],   
                 [ 7,'*', 5 ] ]  

        

        end=    [ [ 1, 2, 3 ],
                  [ 8, '*', 4 ],
                  [ 7, 6, 5 ] ]

        p = game(3)
        p.solve(initial,end)