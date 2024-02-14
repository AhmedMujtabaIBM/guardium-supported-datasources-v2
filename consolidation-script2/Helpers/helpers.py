""" Just a collection of helper functions """
from itertools import product
from typing import List,Callable,Dict,Any


def subtract_lists(list_a:List[List[str]], list_b:List[List[str]]) -> List[List[str]]:
    """ Return A - B, if all elements of B are in A """
    # Check if all elements of list B are in list A
    if all(elem in list_a for elem in list_b):
        # Remove elements of list B from list A
        return [elem for elem in list_a if elem not in list_b]
    else:
        # Return list A unchanged
        return list_a


def product_of_lengths(lists: List[List[str]]) -> int:
    """
    Calculate the product of the lengths of each list in a list of lists.

    Args:
        lists (List[List[Any]]): A list of lists.

    Returns:
        int: The product of the lengths of each list.
    """
    ret_product = 1
    for lst in lists:
        ret_product *= len(lst)
    return ret_product

def combinations(lists:List[List[Any]]) -> List[List[Any]]:
    """ Given a list of lists,
        return every possible permutation when taking an element from each sub-list

    eg. combinations([[1,2,3],["a","b"]]) 
        = [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b'], [3, 'a'], [3, 'b']]
    """
    return [list(comb) for comb in product(*lists)]


def find_ranges(ordered_list):
    """ Given an ordered list, return each possible sub-list
    eg. find_ranges([1,2,3,4]) = 
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
    """
    ranges = [] 
    for i in range(0,len(ordered_list)+1):
        for j in range(i+1,len(ordered_list)+1):
            ranges.append(ordered_list[i:j])

    return ranges


def format_feature_a(key_,original_data):
    for i in original_data:
        if(len(key_) != len(i)):
            raise(TypeError(f"{i} must be same length as {key_} "))
    formatted_data = {}
    
    for i in key_:
        formatted_data[i] = set()

    for entry in original_data:
        for i,x in enumerate(key_):
            formatted_data[x].add(entry[i])
        # database_name, database_version, os_name, os_version = entry
        # formatted_data['DatabaseName'].add(database_name)
        # formatted_data['DatabaseVersion'].add(database_version)
        # formatted_data['OSName'].add(os_name)
        # formatted_data['OSVersion'].add(os_version)
    for i in key_:
        formatted_data[i] = sorted(formatted_data[i])

    return formatted_data

def is_index_between_range(ordered_list, range_tuple, element):
    start_index = ordered_list.index(range_tuple[0])
    end_index = ordered_list.index(range_tuple[1])
    element_index = ordered_list.index(element)
    
    return start_index <= element_index <= end_index


def has_duplicates_2d_lst(list_of_lists:List[List[str]]) -> bool:
    """
    Checks a 2d list for duplicate values
    """
    seen = set()
    for sublist in list_of_lists:
        for item in sublist:
            if item in seen:
                return True
            seen.add(item)
    return False

def has_duplicates_lst(lst:List[str]) -> bool:
    """
    Checks a list for duplicate value
    """
    return len(lst) != len(set(lst))

def group_data_by_feature(data:List[List[str]],get_feature:Callable[[List[str]],str],get_compat:Callable[[List[str]],List[str]]) -> Dict[str,List[str]]:
    """
        Splits a row into compat values and feature values.
        Returns a dict with feature as key, and list of corresponding compats as value.
    """
    ret = {}
    for row in data:
        feature = get_feature(row)
        compat = get_compat(row)
        ret.setdefault(feature, []).append(compat)

    return ret

        