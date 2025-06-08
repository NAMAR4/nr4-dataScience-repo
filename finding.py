

def finding(arr) -> int: 
    numbers = {}
    for element in arr:
        if element in numbers:
            numbers[element] += 1
        else:
            numbers[element] = 1
    
    lone_elem = None
    for elem, amount in numbers.items():
        if amount == 1:
            if lone_elem is not None:           # mehrere elements, die einmal vorkomemn -> None 
                return None
            lone_elem = elem

    return lone_elem