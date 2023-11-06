def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a < b:
        if a < c:
            return a
        else:
            return b
        
    else:
        if b > a:
            return b
        else:
            return a
print(main(1,4,2))
print(main(-5,-3,-1))