1. The sudoku_gen.py takes input from from the input files described as in3.txt(which has n=3 and 3*3 sudoku) and in4.txt(n=4 and 4*4 sudoku).
2. The first line of every inx.txt file contains the size of the sudoku solver followed by the puzzle itself.
3. The python file takes dimension of puzzle in n and in accordance to n the clauses are generated and appended in res variable which holds lists(which are clauses) of lists.
4. Once the clauses are obtained they are fed into the pycosat solver and the clauses are written to an output file (cl.cnf) where all the clauses are encoded in the DIMACS format automatically.
5. The output file cn.cnf when used as the input for the minisat generated the output which is in out.txt file which is another clause.

