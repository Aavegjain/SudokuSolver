from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
        # your code goes here
	row = pos[0]
	col = pos[1]
	result = 1 + 3*((row-1)//3) + (col-1)//3
	return result

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	row_num = pos[0]
	col_num = pos[1]
	row_num2 = (row_num - 1)%3
	col_num2 = (col_num - 1)%3
	index = 1 + 3*row_num2 + col_num2
	return index


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	# your code goes here
	block = []
	block_row = (x-1)//3 + 1
	block_col = (x-1)%3 + 1
	for i in range(0,3):
		row_num = i + (block_row-1)*3
		for j in range(0,3):
			col_num = j + (block_col-1)*3
			block.append(sudoku[row_num][col_num])
	
	return block


def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	# your code goes here

	row = sudoku[i-1]
	return row

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	# your code goes here

	col = list()
	for i in range(0,9):
		col.append(sudoku[i][x-1])
	return col

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku.
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	# your code goes here
	for i in range(0,9):
		for j in range(0,9):
			if sudoku[i][j] == 0:
				return (i+1,j+1)
			


	
	return (-1,-1)

def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid.
	The list will be a single block , single row or single column only.
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	# your code goes here
	arr =[]
	for i in lst:
		if (i != 0):
			if (i in arr):
				return False
			else:
				arr.append(i)
		
			
	
	return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	for i in range(1,10):
		if (not(valid_list(get_row(sudoku,i)))):
			return False

	for i in range(1,10):
		if (not(valid_list(get_column(sudoku,i)))):
			return False

	for i in range(1,10):
		if (not(valid_list(get_block(sudoku,i)))):
			return False
	
	# your code goes here
	return True


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	
	candidate=[]
	
	
	row_index = pos[0]
	col_index = pos[1]
	
	
	'''
	for i in range(1,10):
		counter = 0
		
		for j in range(0,9):
			if (sudoku[row_index-1][j]==i):
				counter = 1
				break

		if (counter == 0):

			for k in range(0,9):
				if (sudoku[k][col_index-1] == i):
					counter = 1
					break
		if (counter == 0):
			x = get_block_num(sudoku,pos)
			block_row = (x-1)//3 + 1
			block_col = (x-1)%3 + 1
			for m in range(0,3):
				row_num = m + (block_row-1)*3
				for n in range(0,3):
					col_num = n + (block_col-1)*3
					if (sudoku[row_num][col_num] == i):
						counter = 1
						break
				if (counter == 1):
					break

		if (counter == 0):
			candidates.append(i)
		
	'''

	

                
                

        

	r = get_row(sudoku,row_index)
	c = get_column(sudoku,col_index)
	b = get_block(sudoku,get_block_num(sudoku,pos))
	for i in range(1,10):
		if (i in c):
			continue
		if (i in r):
			continue
		if (i in b):
			continue
		candidate.append(i)
			
		
	
	
	# your code goes here
	return candidate

	

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
        """This function fill `num` at position `pos` in the sudoku and then returns
        the modified sudoku.
        """
        # your code goes here

        row_index = pos[0]
        col_index = pos[1]
        sudoku[row_index-1][col_index-1] = num
        
        return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you
	did on position `pos` in the sudoku.
	"""
	
	
	# your code goes here
	return make_move(sudoku,pos,0)

def check_sudoku(sudoku,pos,num):
       
        return valid_sudoku( make_move(sudoku,pos,num))
	
	

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	""" This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns
	true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
	It return them in a tuple i.e. `(True, solved_sudoku)`.

	However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
	"""
	# your code goes here

	# to complete this function, you may define any number of helper functions.
	# However, we would be only calling this function to check correctness.
	'''
	pos = find_first_unassigned_position(sudoku)
	if (pos == (-1,-1)):
	    return (True,sudoku)


	i = 0
	l = get_candidates(sudoku,pos)
	
	while i < len(l):
		make_move(sudoku,pos,i)
		response = sudoku_solver(sudoku)
		if (response[0]):
			return response
		i+=1
	undo_move(sudoku,pos)
	return (False,sudoku)'''

	pos = find_first_unassigned_position(sudoku)
	return f(sudoku,pos)
	
                        
                

                
	
        
                
		
			

	

def f(sudoku: List[List[int]],pos: Tuple[int,int])-> Tuple[bool,List[List[int]]]:
	if (pos == (-1,-1)):
			return (True,sudoku)
	i = 0
	l = get_candidates(sudoku,pos)
	while (i<len(l)):
		make_move(sudoku, pos , l[i])
		new_pos = find_first_unassigned_position(sudoku)
		response = f(sudoku,new_pos)
		boolean = response[0]
		if (not boolean):
			i += 1
		else:
			return response
		
	undo_move(sudoku,pos)
	return (False,sudoku)
			
    
               
                               

# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you
# submit your code since it may result in undefined behaviour of the autograder.




'''
sudoku = []
str = "5 3 4 6 7 8 9 1 2 6 7 2 1 9 5 3 4 8 1 9 8 3 4 2 5 6 7 8 5 9 7 6 1 4 2 3 4 2 6 8 5 3 7 9 1 7 1 3 9 2 4 8 5 6 9 6 1 5 3 7 2 8 4 2 8 7 4 1 9 6 3 5 3 4 5 2 8 6 1 7 9"
arr = str.split(' ')
for i in range(0,73,9):
        list2 = list(map(int,arr[i:i+9]))
        sudoku.append(list2)
'''




'''
#print_sudoku(sudoku)
#print(get_block_num(sudoku,(2,6)))

for i in range(1,10):
        for j in range(1,10):
                print(get_position_inside_block(sudoku2,(i,j)))


#print(get_block(sudoku,4))
#print(get_row(sudoku,4))
#print(get_column(sudoku,4))
#print(find_first_unassigned_position(sudoku2))
#print(valid_list([0,0,0,0,0,0,0,0,0]))
#print(valid_sudoku(sudoku2))
'''
#print(get_candidates(sudoku2,(1,3)))
#print(sudoku_solver(sudoku2))
'''
#print_sudoku(make_move(sudoku2,(1,4),6))
#print()
#print_sudoku(make_move(sudoku2,(1,3),4))
#print()
#print_sudoku(undo_move(sudoku2,(1,3)))
#print()
#print_sudoku(undo_move(sudoku2,(1,4)))


tuple = sudoku_solver(sudoku2)
print_sudoku(tuple[1])

     
'''



# Following is the driver code
# you can edit the following code to check your performance.

if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()
        
	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	

	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)



