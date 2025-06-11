import sys

# Code benutzt dieses Finding. Finded das einzelne Element in einer Liste. Prüft, ob es mehrere einzelne Elemente gibt.
def finding(arr) -> int: 
    if not isinstance(arr, list) or any(not isinstance(x, int) for x in arr):
        raise ValueError("Invalid Input")
    
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


# Alternatives kürzeres Finding. Trifft die Annahmen aus der Übung über die Liste
def finding2(arr):
    if not isinstance(arr, list) or any(not isinstance(x, int) for x in arr):
        raise ValueError("Invalid Input")
    result = 0
    for num in arr:
        result ^= num       # XOR a^a=0, a^0=a, kommutativ und assoziativ, alle doppelten heben sich auf
    return result


if __name__ == "__main__":

    input_numbers = [int(x) for x in sys.argv[1:]]
    result = finding(input_numbers)
    print(result)