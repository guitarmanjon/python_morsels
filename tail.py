# For python morsels challenge "tail" - 20th July 2020

# Make a function that takes a sequence (like a list, string, or tuple) and a number n and ... 
#   returns the last n elements from the given sequence, as a list.

def tail(sequence, n):
    # Bonus 2 - works with any iterable
    # Just casting to a list...
    seq = list(sequence)
    
    # Bonus 1 - if n is negative, return an empty list
    if n <= 0:
        return []

    if n > len(seq):
        return seq

    # Base problem
    return list(seq[len(seq)-n:len(seq)])

squares = (n**2 for n in range(10))
print(tail(squares,3))

    