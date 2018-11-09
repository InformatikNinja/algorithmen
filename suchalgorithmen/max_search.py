"""Sortieralgorithmus: Max-Suche.

Weitere Informationen findest du auf:
https://informatik-ninja.de/post/suchalgorithmen-min-max-suche-und-lineare-suche-linear-search
"""


def maxOfArray(A):
    """Durchlaufe die Elemente der Menge und merke das jeweils größte Element.

    Args:
        A (list): Menge A

    Returns:
        tuple: max. von A und Index i, sodass 0 <= i <= len(A) und A[i]==max
            oder 0,-1 falls A leer ist.
    """
    # abbruch, da leeres array.
    if len(A) == 0:
        return 0, -1

    currentMax = A[0]
    indexOfMax = 0

    # durchlaufe array und merke größtest element+index
    for i in range(1, len(A)):
        if A[i] > currentMax:
            currentMax = A[i]
            indexOfMax = i

    return currentMax, indexOfMax


if __name__ == '__main__':
    print(maxOfArray([2, 5, 8, 10, 1, 42, 6]))  # Ausgabe: (42, 5)
