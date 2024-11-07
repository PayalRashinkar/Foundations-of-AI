from collections import deque
import heapq

#parse the input.txt file to get the algorithm type
line = []
with open('input3.txt', 'r') as input_file:
	for every_line in input_file:
		line.append(every_line)


#Getting the global variables and matrix from input.txt file
tmp0 = line[1].split()
mountain_2d = tuple(map(int, tmp0))
col, rows = mountain_2d
tmp1 = line[2].split()
skier_start = tuple(map(int, tmp1))
skier_stamina = int(line[3])
num_lodge = int(line[4])
momentum = 0
moment_dict = {}
new_moment = {}

# create list of list of rows and columns
matrix = []
m_line_num = 5+num_lodge
for i, grid in enumerate(line):
	if i >= m_line_num and i <= m_line_num + rows - 1:
		row = deque(map(int, grid.strip().split()))
		matrix.append(row)


# create list of lodges
lodges = []
for i in range(1, num_lodge+1):
	tmp2 = line[4+i].split()
	tmp3 = tuple(map(int,tmp2))
	lodges.append(tmp3)

#Defining BFS algorithm
def shortest_path(algorithm, skier_start, lodge, matrix):
	algo = algorithm
	visited = set()
	queue = []
	cost = None
	prev_node = {skier_start: None}
	fmeasure = {}
	global moment_dict
	global new_moment
	
	if algo == "BFS\n":
		queue = deque([skier_start])
		visited.add(skier_start)
	elif algo == "UCS\n":
		queue = [(0, skier_start)]
		cost = {skier_start: 0}
	else:
		cost = {skier_start:0}
		moment_dict = {skier_start:0}
		new_moment = {skier_start:0}
		fmeasure = {skier_start:taxicab_distance(skier_start,lodge)}
		heapq.heappush(queue, (fmeasure[skier_start],skier_start))
	
	while queue:
		if algo == "BFS\n":
			latest_node = queue.popleft()
		else:
			latest_cost, latest_node = heapq.heappop(queue)
		if latest_node == lodge:
			road = [latest_node]
			#print(prev_node)
			while road[-1] != skier_start:
				road.append(prev_node[road[-1]])
			return road[::-1]
		
		Eprev = prev_node[latest_node]
		
		if algo == "UCS\n":
			if latest_node not in visited:
				visited.add(latest_node)
		elif algo == "A*\n":
			visited.add(latest_node)
		for neighbor in find_neigh(matrix, latest_node, Eprev, algo):

			if neighbor not in visited or neighbor in new_moment:
				if algo == "BFS\n":
					visited.add(neighbor)
					prev_node[neighbor] = latest_node
					queue.append(neighbor)
				else:
					if neighbor in new_moment and algo == "A*\n":
						if neighbor == Eprev:
							continue
						if new_moment[neighbor] > moment_dict[neighbor] or neighbor in visited:
							cost_update = latest_cost + distance_cost(matrix, latest_node, neighbor, algo)
							if neighbor in cost and cost_update >= cost[neighbor]:
								cost[neighbor] = cost_update
								prev_node[neighbor] = latest_node
								flag = cost_update + taxicab_distance(neighbor, lodge)
								heapq.heappush(queue,(flag, neighbor))
								continue
						
					cost_update = latest_cost + distance_cost(matrix, latest_node, neighbor, algo)
					if neighbor not in cost or cost_update < cost[neighbor]:
						cost[neighbor] = cost_update
						prev_node[neighbor] = latest_node
						if algo == "UCS\n":
							heapq.heappush(queue, (cost_update,neighbor))
						else:
							flag = cost_update + taxicab_distance(neighbor, lodge)
							heapq.heappush(queue,(flag, neighbor))
	return False


#Function to get the neighbors of the latest_node node
def find_neigh(matrix, latest_node, Eprev, algo):
	x, y = latest_node
	neighbors = [(x-1, y-1),(x, y-1),(x+1, y-1),(x+1, y),(x+1, y+1),(x, y+1),(x-1,y+1),(x-1,y)]
	selected_neigh = [(new_x, new_y) for new_x, new_y in neighbors if neigh_check(matrix, new_x, new_y, latest_node, Eprev, algo)] 
	if algo == "A*\n":
		momentum_node(selected_neigh, latest_node, Eprev)
	return selected_neigh

def momentum_node(selected_neigh, latest_node, Eprev):
	a, b = latest_node
	for x, y in selected_neigh:
		if (x, y) not in moment_dict:
			if matrix[y][x] - matrix[b][a] < 0:
				moment_dict[(x, y)] = matrix[b][a] - matrix[y][x]
			else:
				moment_dict[(x, y)] = 0
		else:
			if matrix[y][x] - matrix[b][a] < 0:
				new_moment[(x, y)] = matrix[b][a] - matrix[y][x]
			else:
				new_moment[(x, y)] = 0
			
		

#Function to validate if the neighbor meets the condition of stamina, trees and momentum
def neigh_check(matrix, new_x, new_y, latest_node, Eprev, algo):
	x, y = latest_node
	tree = 0
	global momentum
	
	if 0 <= new_y < len(matrix) and 0 <= new_x < len(matrix[0]):
		if matrix[new_y][new_x] < 0:
			tree = matrix[new_y][new_x] * -1
			if not matrix[y][x] >= tree:
				return False
			else:
				 return True
		else:
			if matrix[y][x] < 0:
				matrix[y][x] *= -1
			if not algo == "A*\n":
				return matrix[new_y][new_x] <= matrix[y][x]+skier_stamina
			else:
				if (matrix[new_y][new_x] - matrix[y][x]) > 0:
					if not Eprev == None:
						a, b = Eprev
						momentum = max(0, matrix[b][a] - matrix[y][x])
					return matrix[new_y][new_x] <= matrix[y][x]+skier_stamina+momentum
				else:
					return matrix[new_y][new_x] <= matrix[y][x]+skier_stamina
				
	else:
		return False

#Function to compute cost incase of UCS and A*, with diagonal being 14 and horizontal and vertical being 10
def distance_cost(matrix, latest_node, neighbor, algo):
	x, y = latest_node
	p, q = neighbor
	EchangeCost = 0
	if not algo == "A*\n":
		if neighbor in [(x-1, y-1),(x+1, y-1),(x+1, y+1),(x-1,y+1)]:
			return 14
		else:
			return 10
	else:
		if not matrix[q][p] - matrix[y][x] > momentum:
			EchangeCost = 0
		else:
			EchangeCost = max(0, matrix[q][p] - matrix[y][x] - momentum)
		if neighbor in [(x-1, y-1),(x+1, y-1),(x+1, y+1),(x-1,y+1)]:
			return 14 + EchangeCost
		else:
			return 10 + EchangeCost

result1 = ""
#Function to write the output to the text file
def output_file(answer):
	global result1
	if answer != False:
		result = " ".join([f"{x},{y}" for x, y in answer])
		result1 += result + "\n"
	else:
		result1 += "FAIL" + "\n"

def taxicab_distance(start, lodge):
	return abs(start[0] - lodge[0]) + abs(start[1] - lodge[1])


#Check the search algorithm being used
if line[0] == "BFS\n":
	for lodge in lodges:
		answer = shortest_path("BFS\n",skier_start, lodge, matrix)
		output_file(answer)
	with open("output.txt", "w") as output:
		output.write(result1)
	result1 = ""
elif line[0] == "A*\n":
	for lodge in lodges:
		answer = shortest_path("A*\n",skier_start, lodge, matrix)
		output_file(answer)
	with open("output.txt", "w") as output:
		output.write(result1)
	result1 = ""
elif line[0] =="UCS\n":
	for lodge in lodges:
		answer = shortest_path("UCS\n",skier_start, lodge, matrix)
		output_file(answer)
	with open("output.txt", "w") as output:
		output.write(result1)
	result1 = ""

