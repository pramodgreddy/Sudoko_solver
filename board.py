import pprint
# board = [
# 	[7,8,0,4,0,0,1,2,0],
# 	[6,0,0,0,7,5,0,0,9],
# 	[0,0,0,6,0,1,0,7,8],
# 	[0,0,7,0,4,0,2,6,0],
# 	[0,0,1,0,5,0,9,3,0],
# 	[9,0,4,0,6,0,0,0,5],
# 	[0,7,0,3,0,0,0,1,2],
# 	[1,2,0,0,0,7,4,0,0],
# 	[0,4,9,2,0,6,0,0,7]
#    ]




board = [[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]
   ]


def plain_board():
	matrix = [] 

	for i in range(9): 
		
		# Append an empty sublist inside the list 
		matrix.append([]) 
		
		for j in range(9): 
			matrix[i].append(0) 
			
	pprint.pprint(matrix) 

   			

   
plain_board()

# [[0, 0, 0, 2, 6, 0, 7, 0, 1],
#  [6, 8, 0, 0, 7, 0, 0, 9, 0],
#  [1, 9, 0, 0, 0, 4, 5, 0, 0],
#  [8, 2, 0, 1, 0, 0, 0, 4, 0],
#  [0, 0, 4, 6, 0, 2, 9, 0, 0],
#  [0, 5, 0, 0, 0, 3, 0, 2, 8],
#  [0, 0, 9, 3, 0, 0, 0, 7, 4],
#  [0, 4, 0, 0, 5, 0, 0, 3, 6],
#  [7, 0, 3, 0, 1, 8, 0, 0, 0]]

[[0, 2, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 6, 0, 0, 0, 0, 3],
 [0, 7, 4, 0, 8, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 3, 0, 0, 2],
 [0, 8, 0, 0, 4, 0, 0, 1, 0],
 [6, 0, 0, 5, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 7, 8, 0],
 [5, 0, 0, 0, 0, 9, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 4, 0]]


# def print_board(bo):
# 	for i in range(len(bo)): #can be range(9) also
# 		if i%3==0 and i!=0:  #to find rows and print -- after every 3 rows
# 			print("-----------------------")
# 		for j in range(len(bo[0])): #to find and print | after every 3 columns
# 			if j%3==0 and j!=0:
# 				print(" | ",end="")

# 			if j==8: #to detect end of column 8 (0-9)
# 				print(bo[i][j]) #print numbers in last column
# 			else:
# 				print(str(bo[i][j])+ " ",end="") #print numbers for all columns except j=8
			
				
# def empty_slot(bo):
# 	for i in range(len(bo)): #in the range(9)
# 		for j in range(len(bo[0])):
# 			if bo[i][j]==0:
# 				return(i,j)

# 	return False			





# print_board(board)
# empty_slot(board)