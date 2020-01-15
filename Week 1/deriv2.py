## Cameron Calv ECE T480

def deriv2(x_vals, function, step_size):
    # Calculate Forward Differences
    forward_diff = []
    for idx in range(len(x_vals)):
        forward_diff.append((function(x_vals[idx]+2*step_size)-2*function(x_vals[idx]+step_size)+function(x_vals[idx]))/(step_size*step_size))

    # Calculate Backward Differences
    backward_diff = []
    for idx in range(len(x_vals)):
        backward_diff.append((function(x_vals[idx])-2*function(x_vals[idx]-step_size)+function(x_vals[idx]-2*step_size))/(step_size*step_size))

    # Calculate Central Differences
    central_diff = []
    for idx in range(len(x_vals)):
        central_diff.append((function(x_vals[idx]+step_size)-2*function(x_vals[idx])+function(x_vals[idx]-step_size))/(step_size*step_size))

    return forward_diff, backward_diff, central_diff

if __name__ == '__main__':
    x_values = []
    for x in range(20):
        x_values.append(x)
    function = lambda x: x*x + 2*x + 1
    step_size = 0.01
    diff = deriv2(x_values, function, step_size)

    print(diff)

