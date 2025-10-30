def hill_climbing(start, step_size=0.1, max_iter=100):
    current = start
    for i in range(max_iter):
        # Check neighbors: current-step and current+step
        left = current - step_size
        right = current + step_size
        
        left_val = f(left)
        right_val = f(right)
        current_val = f(current)
        
        # Find the best neighbor
        if left_val > current_val and left_val >= right_val:
            current = left
        elif right_val > current_val and right_val > left_val:
            current = right
        else:
            # No improvement, stop
            break
        
        print(f"Iteration {i+1}: x = {current}, f(x) = {f(current)}")
    
    return current, f(current)

def f(x):
    # Example function with max at x=3
    return -(x - 3)**2 + 5

# Run hill climbing starting from 0
opt_x, opt_val = hill_climbing(0)
print(f"Optimal x: {opt_x}, Maximum value: {opt_val}")
