


def descending_list_iterator(numbers_list):
    
    #test with empty list
    assert descending_list_iterator([])) == [], "descending_list_iterator does not return the correct value for input []. It sould be [], that is, empty"
    
    #test with a list of one element
    assert descending_list_iterator([7]) == [7], "descending_list_iterator does not return the correct value for input [7]. It sould be [7]"

    #test with a list of multiple elements
    assert descending_list_iterator([5, 1, 8, 3, 2]) == [8, 5, 3, 2, 1], "descending_list_iterator does not return the correct value for input [5, 1, 8, 3, 2]. It sould be [8, 5, 3, 2, 1]"

    #test with a list of repeated elements
    assert descending_list_iterator([1, 1, 1, 1]) == [1, 1, 1, 1], "descending_list_iterator does not return the correct value for input [1, 1, 1, 1]. It sould be [1, 1, 1, 1]"
    
    #test with a list of negative elements
    assert descending_list_iterator([-1, -5, -3, -2]) == [-5, -4, -3, -2], "descending_list_iterator does not return the correct value for input [-1, -5, -3, -2]. It sould be [-5, -4, -3, -2]"
    
