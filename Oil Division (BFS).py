""" This is a classic Search problem.
    First of all we should define a set of states, a set of actions, and a set of capacity.
    Then, we can choose a distinct action as each search step, since the action space is much smaller than the state space.
    Therefore, we can use the chosen actions to decide the transition of states."""
    
from collections import deque

def is_goal(state: deque):
    """
    This works to decide if a state is the goal state.
    """
    if state.count(5) >= 2:
        return 1
    else:
        return 0

def solve_oil_division():
    """
    This works to find the solution to the oil division problem.
    """
    
    # Define the capacity of each busket.
    capacity = (10, 7, 3)
    
    # Define the initial states.
    start = (10, 0, 0)
    
    # Initialize the dequeue, with the start state(10, 0, 0) and the blanket history.
    queue = deque([(start, [])])
    # Initialize the visited list.
    visited = [start]
    
    # Define the action space.
    actions = set([(i, j) for i in range(3) for j in range(3) if i != j ])
    
    
    while queue:
        current_state, path = queue.popleft()
        # Check if the goal is reached.
        if is_goal(current_state):
            return path + [current_state]
        
        # Generate all child states.
        for source, target in actions:
            # Check if the source busket is empty or the target busket is full.
            if current_state[source] == 0 or current_state[target] == capacity[target]:
                continue
            else:
                change = min(current_state[source], capacity[target] - current_state[target])
            # Calculate the new state.
            new_state = list(current_state)
            new_state[source] -= change
            new_state[target] += change
            # Check if the new state has been passed by.
            if new_state not in visited:            
                # Add the new state to the dequeue and the passed path to the visited list.
                queue.append((tuple(new_state), path + [current_state]))
                visited.append(new_state)
        
    # If no solution is found after the complete loop on the whole state space.
    return None

def print_solution(solution):
    """This works to show the solution path."""
    if not solution:
        print("No solution found!")
        return
    
    print("Solution found!\nSteps:")
    print("Format: (Busket1, Busket2, Busket3)")
    print("-" * 40)
    
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
        
        if i < len(solution) - 1:
            # Show the pour operation
            current = solution[i]
            next_state = solution[i + 1]
            
            # Find which buckets changed
            changes = []
            for j in range(3):
                if current[j] != next_state[j]:
                    changes.append(j)
            
            if len(changes) == 2:
                from_bucket = changes[0] if current[changes[0]] > next_state[changes[0]] else changes[1]
                to_bucket = changes[1] if from_bucket == changes[0] else changes[0]
                amount = abs(current[from_bucket] - next_state[from_bucket])
                
                bucket_names = ["Busket1", "Busket2", "Busket3"]
                print(f"      → Pour {amount} from {bucket_names[from_bucket]} to {bucket_names[to_bucket]}")



# Solve and display the solution
solution = solve_oil_division()
print_solution(solution)
                
                
                
            
        
        
        
    
