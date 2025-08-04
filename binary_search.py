def binary_search_iterative(arr, target):
    """
    Iterative implementation of binary search.
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive implementation of binary search.
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
        left: Left boundary (default: 0)
        right: Right boundary (default: len(arr) - 1)
    
    Returns:
        Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Example usage and testing
if __name__ == "__main__":
    # Test array (must be sorted for binary search)
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("Test Array:", test_array)
    print()
    
    # Test cases
    test_targets = [7, 1, 19, 4, 20]
    
    for target in test_targets:
        # Test iterative version
        result_iter = binary_search_iterative(test_array, target)
        
        # Test recursive version
        result_rec = binary_search_recursive(test_array, target)
        
        print(f"Searching for {target}:")
        print(f"  Iterative result: {result_iter}")
        print(f"  Recursive result: {result_rec}")
        
        if result_iter != -1:
            print(f"  Found at index {result_iter}, value: {test_array[result_iter]}")
        else:
            print(f"  Not found in array")
        print()