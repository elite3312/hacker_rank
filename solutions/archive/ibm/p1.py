import math

def find_smallest_divisor(arr, threshold):
    """
    Uses binary search to find the smallest divisor such that:
      sum(math.ceil(num / divisor) for num in arr) <= threshold
    
    If you require the condition sum < threshold (strictly less than),
    change the condition inside the binary search accordingly.
    """
    low, high = 1, max(arr)
    
    while low <= high:
        mid = (low + high) // 2
        total = sum(math.ceil(num / mid) for num in arr)
        
        # If total is within the threshold, this divisor works.
        # Try to see if a smaller divisor can also satisfy the condition.
        if total <= threshold:
            high = mid - 1
        else:
            # Otherwise, increase the divisor, because a larger divisor 
            # will decrease the total sum.
            low = mid + 1
            
    return low

def main():
    try:
        # Expecting the user to enter array elements separated by spaces.
        arr_input = input("Enter array elements separated by spaces: ").strip()
        threshold_input = input("Enter threshold: ").strip()
        arr = list(map(int, arr_input.split()))
        threshold = int(threshold_input)
    except Exception as e:
        print("Invalid input. Please ensure you enter integers correctly.")
        return
    
    # Calculate the smallest divisor using our helper function.
    result = find_smallest_divisor(arr, threshold)
    print("The smallest divisor is:", result)

if __name__ == '__main__':
    main()