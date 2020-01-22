## Cameron Calv ECE T480
# Finds regions of roots using the incremental area. Requires the function(anonymous),
# upper and lower limit, and the number of regions between the limits as input. The output
# should be an array of regions where there are zero crossings.

def incremental(function_handle, upper_limit, lower_limit, num_of_regions):
    if(upper_limit < lower_limit):
        temp = upper_limit
        upper_limit = lower_limit
        lower_limit = temp
    if(upper_limit != lower_limit):
        zero_crossing_regions = []
        step_size = abs(upper_limit - lower_limit)/num_of_regions
        regions_endpoints = []
        next_endpoint = lower_limit
        while(next_endpoint < upper_limit):
            regions_endpoints.append(next_endpoint)
            next_endpoint += step_size
        regions_endpoints.append(upper_limit)
        for idx in range(len(regions_endpoints)-1):
            lower_endpoint = regions_endpoints[idx]
            upper_endpoint = regions_endpoints[idx+1];
            lower_value = function_handle(lower_endpoint)
            upper_value = function_handle(upper_endpoint)
            if((lower_value * upper_value) < 0):
                zero_crossing_regions.append([lower_endpoint, upper_endpoint])
        return zero_crossing_regions
    else:
        return []


if __name__ == '__main__':
    function = lambda x: (x**3 + 2*(x**2) - 5*x - 6)
    print("Brackets of Potential Roots:")
    output = incremental(function, -4, 4, 301)
    for bracket in output:
        print(bracket)