import pycosat
res=[]
CNF=[]
#Every boolean variable(n^6 in number) can be represend by a number between 1 to n^6
def v(i,j,d,n): #it returns the variable number of the boolean variable under consideration
    return (n**4)*(i-1)+n*n*(j-1)+d
#this function(validity) returns the clauses of 2 variables no repition of a value in a row , column or an n*n cell
#the number v(i,j,d) represents the variable i.e xij=d hence we must take negation i.e our clause will become
# -v(i,j,d) where i,j,d will run from 1 to n*n.     
def validity(cell,n):
    for i,xi in enumerate(cell):
        for j,xj in enumerate(cell):
            if i<j:
                for d in range(1,(n*n)+1):
                    res.append([-v(xi[0],xi[1],d,n),-v(xj[0],xj[1],d,n)])
def sudoku_solve(n):
    #adding clauses which ensure that each row,column gets atleast one value i.e xij=d or v(i,j,d)(+ve for boolean true)
    #each clause length will be n*n
    for i in range(1,(n*n)+1):
        for j in range(1,(n*n)+1):
            res.append([v(i,j,d,n) for d in range(1,(n*n)+1)])
            for d in range(1,(n*n)+1):
                #this ensures that an unique does not get more than one value at a time 
                #again represented as a boolean variable v(i,j,d) meaning xij=d so negation will be
                #-v(i,j,d) which means xij not equal to d and each clause has 2 literals.
                for dahead in range(d+1,(n*n)+1):
                    res.append([-v(i,j,d,n),-v(i,j,dahead,n)])
    for i in range(1,(n*n)+1):
        validity([(i,j) for j in range(1,(n*n)+1)],n)
        validity([(j,i) for j in range(1,(n*n)+1)],n)
    c=1
    l=[]
    l.append(1)
    for i in range(1,n):
        c+=n
        l.append(c)
        #additional validity function call to ensure no repetition in each cell
    for i in l:
        for j in l:
            validity([(i+k%n,j+k//n) for k in range(n*n)],n)
    return res
def solve(grid,n):
    CNF = sudoku_solve(n) #contains all the clauses which will be fed into the sudoku solver
    for i in range(1,(n*n)+1):
        for j in range(1,(n*n)+1):
            if grid[i-1][j-1]>0:
                CNF.append([v(i,j,grid[i-1][j-1],n)])
    sol = pycosat.solve(CNF)
    def read_cell(i,j,n):
        for d in range(1, (n*n)+1):
            if v(i, j, d , n) in sol:
                return d
    for i in range(1, (n*n)+1):
        for j in range(1, (n*n)+1):
            grid[i - 1][j - 1] = read_cell(i,j,n)
if __name__=="__main__":

    l=[]
    file = open("in4.txt","r")
    for i in file:
        l.append(i)
    file.close()
    c=0
    n=0
    hard=[]
    aux=[]
    for i in l:
        if c==0:
            n=int(i[0])
            c=1
        else:
            aux=list(map(int,i.split(" ")))
            hard.append(aux)
            aux=[]
    print("the sudoku puzzle is\n")
    for i in hard:
        print(i)
    solve(hard,n)
    print("the solved sudoku is\n")
    for i in hard:
        print(i)
    print("\n writing all the clauses in the file cl.cnf")
    file = open("cl.cnf","w")
    var1 = str(n**6)
    var2 = str(len(res))
    s = "p cnf "
    s = s + var1 +" "+ var2
    s = s + "\n"
    file.write(s)
    for i in res:
        l = i
        s=""
        l.append(0)
        for j in l:
            s+=str(j)+" "
        s = s + "\n"
        file.write(s)
    file.close()