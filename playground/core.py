
def find_black_peaks(list_of_intensities):
    """Find peaks

    Find local minima or blackness maxima for a given list of color tupels. 
    color tupels are defined as local maxima if the 
    sum of all 3 intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_colors (list of tupels of 3 ints): a list of
            numeric values in tupels

    Returns:
        list of floats: list of the identified local maxima positions

    Note:
        This is just a place holder for the TDD part :)
    """
    
    blackness_list = []
    for pixels in list_of_intensities:
        blackness_list.append(sum(pixels))
    #print(blackness_list)
    list_of_maxima = []
    for pos, element in enumerate(blackness_list):
        if pos == 0:
            continue
        if pos == len(blackness_list) - 1:
            continue
        if blackness_list[pos - 1] > element < blackness_list[pos + 1]:
            max_value = element
            list_of_maxima.append(max_value)
    return list_of_maxima
