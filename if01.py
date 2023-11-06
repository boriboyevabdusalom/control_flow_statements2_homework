def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b:
        if a > c:
            return a
        else:
            return b

    else:
        if c > b:
           return c 
        else:
            return b 
print(main(1,4,2))
print(main(-5,-3,-1))