import pprint
board =[[0, 2, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 6, 0, 0, 0, 0, 3],
 [0, 7, 4, 0, 8, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 3, 0, 0, 2],
 [0, 8, 0, 0, 4, 0, 0, 1, 0],
 [6, 0, 0, 5, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 7, 8, 0],
 [5, 0, 0, 0, 0, 9, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 4, 0]]

def logic(bo):
	
	find= empty_slot(bo)				#assigning find the result of empty_slot function(either the tuple or False)
	if not find:						#checking if all slots are filled
		return True
	else:								#if not filled then take the values of tuple
		row,col=find

	for i in range(1,10):				#checking in the range of 1-9 
		if check_valid(bo,i,(row,col)): #run the function check_valid with parameters
			bo[row][col]=i 				#fill in the slot in the board with new value

			if logic(bo):				#re run the function with new value and check if its new slot value is correct	
				return True

			bo[row][col]=0				#if the value is not correct,reset it to 0 

	return False


#Function to check if we ca place a valid number in slot(returned by empty_slot fn)
def check_valid(bo, num, pos):
	#to Check if a number can be placed in the row
	for i in range(len(bo[0])):
		if bo[pos[0]][i]==num and  pos[1]!=i: 		#checking if num can be placed in the row
			return False

	#to check if a number can be placed in a column
	for i in range(len(bo)):
		if bo[i][pos[1]]==num and pos[0]!=i:		#checking if num can be placed in the column
			return False

	#to check if a number can be placed in 3*3 cubes
	box_x=pos[1]//3			 						#assigning box_x the value of columnn of the cubes
	box_y=pos[0]//3									#assigning box_y the value of row of the cubes

	for i in range(box_y*3,box_y*3+3):				#checking in the range of a rows of a cube
		for j in range(box_x*3,box_x*3+3):			#checking in the range of columns of a cube
			if bo[i][j]==num and (i,j)!=pos:		#checking if num can be placed in that position
				return False

	return True





# def print_board():
#   pprint.pprint(board)
#Function to print Board
def print_board(bo):
	for i in range(len(bo)): #can be range(9) also
		if i%3==0 and i!=0:  #to find rows and print -- after every 3 rows
			print("-----------------------")
		for j in range(len(bo[0])):              #to find and print | after every 3 columns
			if j%3==0 and j!=0:
				print(" | ",end="")

			if j==8:                             #to detect end of column 8 (0-9)
				print(bo[i][j])                  #print numbers in last column
			else:
				print(str(bo[i][j])+ " ",end="") #print numbers for all columns except j=8
			
#Function to check if a slot is empty
def empty_slot(bo):
	for i in range(len(bo)):        #in the range(9)
		for j in range(len(bo[0])): #in the range(9)
			if bo[i][j]==0:         # check if the slot has value 0
				return(i,j)			#if value is 0 return the position as a tuple

	return False					#if slot has non-zero value return false



# print_board(board)
# empty_slot(board)
print("Board before Solving:")
print_board(board)
logic(board)
print("------------------------------------")
print("Board after Solving")
print_board(board)