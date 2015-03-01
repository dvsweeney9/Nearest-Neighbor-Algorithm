## NEAREST NEIGHBOUR ALGORITHM FOR TRAVELING SALESMAN PROBLEM

## SET VARIABLES;
import copy;
import time;

matrix = [[0 for x in range(10)] for j in range(10)];

matrix[0] = [0,40,30,50,0,0,0,0,0,0];
matrix[1] = [40,0,30,0,60,0,0,0,0,0];
matrix[2] = [30,30,0,40,0,60,0,0,0,0];
matrix[3] = [50,0,40,0,0,0,30,0,0,0];
matrix[4] = [0,60,0,0,0,40,0,30,0,0];
matrix[5] = [0,0,60,0,40,0,90,0,70,0];
matrix[6] = [0,0,0,30,0,90,0,0,0,80];
matrix[7] = [0,0,0,0,30,0,0,0,60,0];
matrix[8] = [0,0,0,0,0,70,0,60,0,50];
matrix[9] = [0,0,0,0,0,0,80,0,50,0];

path = [0]*1;
weight = 0;

visited = [0,0,0,0,0,0,0,0,0,0];

dirty = [];
temp = 0;

complete = False;
backtrack = False;

temp = 0;
pivot = False;

# 1: Stand on an arbitrary vertex as current vertex;
start = 0;
current = start;
path[0] = start;
visited[0] = 1;

while(complete == False) :

	print("Current path = ", path);
	print("Current visits = ", visited);
	print("Current weight = ", weight);
	print("\n");

	## PIVOT = FURTHEST BACK YOU WENT BEFORE YOU STARTED MOVING FORWARD AGAIN. 
	## WHERE DO YOU SET THIS?!?!

	if (backtrack == True) :
		## Backtrack. reverse last step. set edge to dirty. 

		visited[current] = 0;

		if (len(path) > 1) :
			weight = weight - matrix[path[-1]][path[-2]];

		path.pop();
		current = path[-1];


		temp = current;
		
		backtrack = False;

	# 2: Find out the shortest edge connecting current vertex and an unvisited vertex 		

	minEdge = 100000;
	closestVertex = 0;

	for i in range(len(matrix[current])) :
		if ((matrix[current][i] != 0) and (matrix[current][i] < minEdge)) :
			tempPath = [];
			tempPath = copy.copy(path);
			tempPath.append(i);
			if tempPath in dirty :
				dirtyBool = True;
			else :
				dirtyBool = False;
			if (visited[i] == 0) and (dirtyBool == False) :
				closestVertex = i;
				minEdge = matrix[current][i];

	if (minEdge == 100000) :
		backtrack = True;

	if (backtrack == True) :
		continue;

	weight = weight + minEdge;
	path.append(closestVertex);

	# 3: Set Current Vertex to V
	current = closestVertex;

	if pivot == True :
		dirty.append(copy.copy(path));
		pivot = False;

	if (temp == path[-2]) :
		pivot = True;

	# 4: mark V as visited
	visited[closestVertex] = 1;

	#5: if all vertices in domain are visited, then terminate.
	if (visited[5] == 1) and (visited[7] == 1) and (visited[9] == 1) and (matrix[path[-1]][0] != 0) :
		complete = True;


weight= weight + matrix[path[-1]][0];
print "-------FINAL PATH-------"
print "PATH IS: "
pathq=''
for i in range(9) :
	pathq+=str(path[i] + 1)+' => ';
print pathq + '1'
print "TOTAL WEIGHT IS: " + str(weight);
time.sleep(10);

