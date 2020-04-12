"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    falling_factorial = 1
    while k > 0:
        falling_factorial *= n
        k -= 1
        n -= 1
    return falling_factorial

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    previous_is_eight = False
    
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and previous_is_eight:
            return True
        elif last_digit == 8:
            previous_is_eight = True
        else:
            previous_is_eight = False
        n //= 10
    return False
