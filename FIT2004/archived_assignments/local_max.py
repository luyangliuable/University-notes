import random
import time


def find_local_max(M: list[list[int]]) -> list[int]:
    """
    This function finds and returns one local minimum of a N*N matrix. It does this by finding the next maximum in its from current position to surroundings and traverse to the next one until it finds one without any local maximum.

        # TODO
        # Check if it is required to output more than one local maximum
        # Check if it is required to change time complexity and algorithm to use less if statements

        Parameters:
        M (list[list[int]]): A matrix of size n*n containing integers

        Returns:
        An array (list[int]) containing int that corresponds to the position of the local maximum


        Time Complexity for finding single local maximum:
            Worse case: O(N)
            Best case: O(N)

        Space complexity:
            Worse case: O(1)
    """

    ###############################################################################
    #                  Start with the 0,0 position on the matrix                  #
    ###############################################################################
    i = 0
    j = 0

    ###############################################################################
    #                     Stop until reaching a local maximum                     #
    ###############################################################################
    while True:
        if i > 0 and i < len(M) - 1 and j < len(M[i])-1 and j > 0:
            surrounding_coord = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i == 0 and j < len(M[i])-1 and j > 0:
            surrounding_coord = [[i+1, j], [i, j+1], [i, j-1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i == len(M)-1 and j < len(M[i])-1 and j > 0:
            surrounding_coord = [[i-1, j], [i, j+1], [i, j-1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i > 0 and i < len(M)-1 and j == 0:
            surrounding_coord = [[i-1, j], [i, j], [i, j], [i, j+1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i > 0 and i < len(M)-1 and j == len(M[i])-1:
            max_index = 0
            surrounding_coord = [[i+1, j], [i-1, j], [i, j-1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i == len(M)-1  and j == len(M[i])-1:
            max_index = 0
            surrounding_coord = [[i-1, j], [i, j-1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i == 0 and j == len(M[i])-1:
            surrounding_coord = [[i+1, j], [i, j-1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i == 0 and j == 0:
            surrounding_coord = [[i+1, j], [i, j+1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i == len(M) - 1  and j == 0:
            surrounding_coord = [[i-1, j], [i, j+1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]

        if i == len(M) - 1  and j == len(M[i])-1:
            surrounding_coord = [[i-1, j], [i, j-1]]
            max_index = find_max(M, surrounding_coord)
            if M[surrounding_coord[max_index][0]][surrounding_coord[max_index][1]] > M[i][j]:
                i = surrounding_coord[max_index][0]
                j = surrounding_coord[max_index][1]
            else:
                return [i, j]


def get_surrounding_coord(M) -> list[list[int]]:
    surrounding_coord = []

    if i > 0 and i < len(M) - 1 and j < len(M[i])-1 and j > 0:
        surrounding_coord = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
        return surrounding_coord

    if i == 0 and j < len(M[i])-1 and j > 0:
        surrounding_coord = [[i+1, j], [i, j+1], [i, j-1]]
        return surrounding_coord

    if i == len(M)-1 and j < len(M[i])-1 and j > 0:
        surrounding_coord = [[i-1, j], [i, j+1], [i, j-1]]
        return surrounding_coord

    if i > 0 and i < len(M)-1 and j == 0:
        surrounding_coord = [[i-1, j], [i, j], [i, j], [i, j+1]]
        return surrounding_coord

    if i > 0 and i < len(M)-1 and j == len(M[i])-1:
        surrounding_coord = [[i+1, j], [i-1, j], [i, j-1]]
        return surrounding_coord

    if i == len(M)-1  and j == len(M[i])-1:
        surrounding_coord = [[i-1, j], [i, j-1]]
        return surrounding_coord

    if i == 0 and j == len(M[i])-1:
        surrounding_coord = [[i+1, j], [i, j-1]]
        return surrounding_coord

    if i == 0 and j == 0:
        surrounding_coord = [[i+1, j], [i, j+1]]
        return surrounding_coord

    if i == len(M) - 1  and j == 0:
        surrounding_coord = [[i-1, j], [i, j+1]]
        return surrounding_coord

    if i == len(M) - 1  and j == len(M[i])-1:
        surrounding_coord = [[i-1, j], [i, j-1]]
        return surrounding_coord

    return surrounding_coord

def find_max(M: list[list[int]], surrounding_coord: list[list[int]]) -> int:
    """
    Gets a NxN matrix and a list of coordinates that is supposed to surround the current position on the matrix, then return the maximum number out of all the numbers inside the surrounding coordinates.

    parameters:
        M (list[list[int]]): a NxN matrix that contains integers
        surrounding_coord (list[list[int]]): a list of coordinates that contains a list of surrounding coordinates on the matrix

    Returns:
        surrounding_max (int): the maximum number in the list of surrounding coordinates

    Time Complexity for finding single local maximum:
        Worse case: O(4) = O(1) There are 4 coordinates surrounding a spot on the matrix if 0 < i < N and 0 < j < N
        Best case: O(2) = O(1) There are 2 coordinates surrounding a spot on the matrix if i < N and 0 < j < N

    Space complexity:
        Worse case: O(1)
    """

    surrounding_max = 0 # kick start with the treating first item in the surrounding_coord as max then compare the rest
    for i in range(1,len(surrounding_coord)):
        if M[surrounding_coord[i][0]][surrounding_coord[i][1]] > M[surrounding_coord[surrounding_max][0]][surrounding_coord[surrounding_max][1]]:
            surrounding_max = i

    return surrounding_max
