# Problem 6
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L)
# mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    reverseL = []
    reverseElement = []

    for list in L[::-1]:
        reverseL += [list,]

    for element in reverseL:
        reverseElement += [element[::-1],]

    L[:] = reverseElement






# Unit Test
L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
print(L)