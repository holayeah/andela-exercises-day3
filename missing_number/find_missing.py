
def find_missing(arr1, arr2):
    """
    Finds an element missing from arr1 that is in arr2
    """
    
    for value in arr2:
        if not value in arr1:
            return value
    
    return 0
