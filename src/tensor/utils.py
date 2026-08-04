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