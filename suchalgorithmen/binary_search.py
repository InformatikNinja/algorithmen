# -*- coding: utf-8 -*-
"""Sortieralgorithmus: Binäre Suche (binary search).

Weitere Informationen findest du auf:
https://informatik-ninja.de/post/suchalgorithmen-binaere-suche-binary-search
"""


def binary_search_start(A, key):
    """Binäre Suche mit Rekursion.

    Startet die Rekursion.

    Args:
        A (list): Menge A
        key (object): Element das gefunden werden soll.

    Returns:
        Index i, sodass 0 <= i < len(A) und A[i] == key, oder -1 falls key nicht auftritt.
    """
    if len(A) == 0:
        # key wurde nicht gefunden, da liste leer
        return -1
    if len(A) == 1:
        # liste hat nur 1 Element, entweder im Index 0 vorhanden oder nicht.
        if A[0] == key:
            return 0
        else:
            return -1

    # Starte Rekursion
    return binary_search_work(A, key, 0, len(A)-1)


def binary_search_work(A, key, left, right):
    """Binäre Suche mit Rekursion.

    Args:
        A (list): Menge A
        key (object): Element das gefunden werden soll.
        left (int): Linke Grenze der Menge.
        right (int): Rechte Grenze der Liste.

    Returns:
        Index i, sodass 0 <= i < len(A) und A[i] == key, oder -1 falls key nicht auftritt.
    """
    if right < left:
        # key wurde nicht gefunden
        return -1

    middle = int((left + right) / 2)
    if key < A[middle]:
        # key vermutlich in der linken seite -> anpassen der rechten grenze
        return binary_search_work(A, key, left, middle-1)
    if key > A[middle]:
        # key vermutlich in der rechten seite -> anpassen der linken grenze
        return binary_search_work(A, key, middle+1, right)

    # key wurde gefunden
    return middle


def binary_search(A, key):
    """Binäre Suche ohne Rekursion.

    Suche das Element key in der Menge A und gebe den Index des gefundenen Elements zurück.

    Args:
        A (list): Menge A
        key (object): Element das gefunden werden soll.

    Returns:
        int: Index i, sodass 0 <= i < len(A) und A[i] == key, oder -1 falls key nicht auftritt.
    """
    # Grenzen bestimmen
    left = 0
    right = len(A) - 1

    while left <= right:
        middle = int((left + right) / 2)  # Mitte der Liste (abgerundet)

        if key < A[middle]:
            # key vermutlich in der linken seite -> anpassen der rechten grenze
            right = middle - 1
        elif key > A[middle]:
            # key vermutlich in der rechten seite -> anpassen der linken grenze
            left = middle + 1
        else:
            # key wurde gefunden
            return middle

    # key wurde nicht gefunden
    return -1


if __name__ == '__main__':
    data = [12, 17, 23, 24, 31, 32, 36, 37, 42, 47, 53, 55, 64, 75, 89, 91, 91, 93, 96]
    print('Binäre Suche mit Rekursion:', binary_search_start(data, 32))
    print('Binäre Suche ohne Rekursion:', binary_search(data, 32))
