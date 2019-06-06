import pycosat
res=[]
def v(i,j,d):
    return 81*(i-1)+9*(j-1)+d
def validity(cell):
    for i,xi in enumerate(cell):
        for j,xj in enumerate(cell):
            if i<j:
                for d in range(1,10):
                    res.append([-v(xi[0],xi[1],d),-v(xj[0],xj[1],d)])
def sudoku_solve():
    for i in range(1,10):
        for j in range(1,10):
            res.append([v(i,j,d) for d in range(1,10)])
            for d in range(1,10):
                for dahead in range(d+1,10):
                    res.append([-v(i,j,d),-v(i,j,dahead)])
    for i in range(1,10):
        validity([(i,j) for j in range(1,10)])
        validity([(j,i) for j in range(1,10)])
    validity([(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)])
    validity([(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)])
    validity([(1,7),(1,8),(1,9),(2,7),(2,8),(2,9),(3,7),(3,8),(3,9)])
    validity([(4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(6,1),(6,2),(6,3)])
    validity([(4,4),(4,5),(4,6),(5,4),(5,5),(5,6),(6,4),(6,5),(6,6)])
    validity([(4,7),(4,8),(4,9),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9)])
    validity([(7,1),(7,2),(7,3),(8,1),(8,2),(8,3),(9,1),(9,2),(9,3)])
    validity([(7,4),(7,5),(7,6),(8,4),(8,5),(8,6),(9,4),(9,5),(9,6)])
    validity([(7,7),(7,8),(7,9),(8,7),(8,8),(8,9),(9,7),(9,8),(9,9)])
    return res
def solve(grid):
    CNF = sudoku_solve()
    for i in range(1,10):
        for j in range(1,10):
            if grid[i-1][j-1]>0:
                CNF.append([v(i,j,grid[i-1][j-1])])
    sol = pycosat.solve(CNF)
    def read_cell(i, j):
        for d in range(1, 10):
            if v(i, j, d) in sol:
                return d

    for i in range(1, 10):
        for j in range(1, 10):
            grid[i - 1][j - 1] = read_cell(i, j)
if __name__=="__main__":
    l = []
    hard = [[0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 3],
            [0, 7, 4, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 2],
            [0, 8, 0, 0, 4, 0, 0, 1, 0],
            [6, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 7, 8, 0],
            [5, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0]]
    solve(hard)
    for i in hard:
        print(i)
    