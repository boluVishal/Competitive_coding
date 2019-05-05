a,b = input().split()
a = int(a)
b = int(b)

li = []
for i in range(a):
    c = input().split()
    li.append(c)
allPaths = [] 
def findPaths(maze,m,n): 
	path = [0 for d in range(m+n-1)] 
	findPathsUtil(maze,m,n,0,0,path,0) 
	
def findPathsUtil(maze,m,n,i,j,path,indx): 
	global allPaths 
	if i==m-1: 
		for k in range(j,n): 
			path[indx+k-j] = maze[i][k] 
		#print(path) 
		allPaths.append(path) 
		return
	if j == n-1: 
		for k in range(i,m): 
			path[indx+k-i] = maze[k][j] 
		#print(path) 
		allPaths.append(path) 
		return
	

	path[indx] = maze[i][j] 
	
	findPathsUtil(maze, m, n, i+1, j, path, indx+1) 
	
	findPathsUtil(maze, m, n, i, j+1, path, indx+1)
findPaths(li,a,b) 
print(''.join(sorted(min(allPaths))))