def reverse_sort_dictionary(input_dict):
    
    sorted_keys = sorted(input_dict.keys(), reverse=True)
    
    #in the example, it uses a tuple, so we create a tuple, so for each key
    #and their content, we create a new tuple in reverse sorted order
    newTuple = [(key, input_dict[key][0]) for key in sorted_keys] 
    return newTuple

