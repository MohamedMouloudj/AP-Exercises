def length(lst):
    """
    Returns number of elements in a list.
    """
    if lst == []:
        return 0
    return 1 + length(lst[1:])

def mean(lst):
    """
    Returns the mean of a list of numbers.
    """
    return sum(lst) / length(lst)

def range_of_list(lst):
    """
    Returns the difference between max and min values of a list.
    """
    return max(lst) - min(lst)

test= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(length(test))
print(mean(test))
print(range_of_list(test))