import heapq

# Define puzzle states
initial_state = [1, 2, 3, 4, 0, 5, 7, 8, 6]  # 0 represents blank
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

class PuzzleNode:
    def __init__(self, state, parent, move, depth):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = depth + self.heuristic()
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        for i in range(9):
            if self.state[i] != 0:
                current_row, current_col = i // 3, i % 3
                goal_index = goal_state.index(self.state[i])
                goal_row, goal_col = goal_index // 3, goal_index % 3
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance
    
    def get_children(self):
        children = []
        blank_index = self.state.index(0)
        row, col = blank_index // 3, blank_index % 3
        
        # Define possible moves: up, down, left, right
        moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
        
        for dr, dc, move_name in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = self.state[:]
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
                children.append(PuzzleNode(new_state, self, move_name, self.depth + 1))
        
        return children

def solve_puzzle():
    start_node = PuzzleNode(initial_state, None, None, 0)
    
    if start_node.state == goal_state:
        return [start_node]
    
    open_list = []
    heapq.heappush(open_list, start_node)
    closed_set = set()
    
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(tuple(current_node.state))
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]
        
        for child in current_node.get_children():
            if tuple(child.state) not in closed_set:
                heapq.heappush(open_list, child)
    
    return None

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Solve and display
solution = solve_puzzle()

if solution:
    print(f"Solution found in {len(solution) - 1} moves:\n")
    for step, node in enumerate(solution):
        if node.move:
            print(f"Move {step}: {node.move}")
        print_state(node.state)
else:
    print("No solution found!")
