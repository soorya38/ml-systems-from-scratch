def infer_shape(data):
    """
    Infers the shape of the given data.
    """
    if isinstance(data, (int, float)):
        return ()
    
    if isinstance(data, list):
        if len(data) == 0:
            return (0, )
        
        first_shape = infer_shape(data[0])

        for item in data:
            if infer_shape(item) != first_shape:
                raise ValueError("All elements must have the same shape")
        
        return (len(data), ) + first_shape
    
    raise ValueError(f"Unsupported data type: {type(data)}")

def numel(data):
    """
    Calculates the number of elements in the given data.
    """
    shape = infer_shape(data)

    numel = 1
    for dim in shape:
        numel *= dim

    return numel

def infer_dtype(data):
    """
    Infers the data type of the given data.
    """
    if isinstance(data, (int, float)):
        return type(data)
    
    if isinstance(data, list):
        if len(data) == 0:
            raise ValueError("Empty list has no data type")
        
        first_dtype = infer_dtype(data[0])

        for item in data:
            if infer_dtype(item) != first_dtype:
                raise ValueError("All elements must have the same data type")
        
        return first_dtype
    
    raise ValueError(f"Unsupported data type: {type(data)}")

def flatten(data):
    """
    Flattens the given data into a 1D list.
    """

    if isinstance(data, (int, float)):
        return [data]
    
    if len(data) == 0:
        return []
    
    return flatten(data[0]) + flatten(data[1:])