"""Sortieralgorithmus: Lineare Suche (linear search).

Weitere Informationen findest du auf:
https://informatik-ninja.de/post/suchalgorithmen-min-max-suche-und-lineare-suche-linear-search
"""


def linear_search(A, key):
    """Lineare Suche.

    Args:
        A (list): Menge A.
        key (object): Element das gefunden werden soll.

    Returns:
        int: Index i, sodass 0 <= i <= len(A) und A[i]==key
            oder -1 falls key nicht auftritt.
    """
    for i in range(len(A)):
        if A[i] == key:
            return i

    return -1


if __name__ == '__main__':
    print(linear_search([2, 5, 8, 10, 1, 42, 6], 10))  # Ausgabe: 3
