"""
Python Sorting Algorithm (Without Built-in Sort)

Custom implementation of selection sort without using Python's
built-in sort() or sorted() functions.
"""


def selection_sort(lst):
    """
    Sort a list from smallest to largest using selection sort algorithm.
    
    Args:
        lst: List of comparable elements
        
    Returns:
        New sorted list (original list is not modified)
    """
    if not lst:
        return []
    
    sorted_list = []
    working_list = lst.copy()
    
    while working_list:
        minimum = working_list[0]
        for element in working_list:
            if element < minimum:
                minimum = element
        sorted_list.append(minimum)
        working_list.remove(minimum)
    
    return sorted_list


if __name__ == "__main__":
    # Example usage
    numbers = [64, 34, 25, 12, 22, 11, 90]
    letters = ['c', 'l', 'y', 'z', 'x', 'o', 'a', 'b']
    
    print("Numbers:", selection_sort(numbers))
    print("Letters:", selection_sort(letters))
