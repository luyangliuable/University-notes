def find_local_max(M: list[list[int]]) -> list[int]:
    """
    This function finds and returns one local minimum of a N*N matrix.

        # TODO
        # Check if it is required to output more than one local maximum
        # Check if it is required to change time complexity and algorithm to use less if statements

        Parameters:
        M (list[list[int]]): A matrix of size n*n containing integers

        Returns:
        An array containing int that corresponds to the position of the local maximum


        Time Complexity:
            Worse case: O(N*N)
            Best case: O(N*N)
            Find single local max: O(N)

        Space complexity:
            Worse case: O(1)
    """
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i > 0 and i < len(M) - 1 and j < len(M[i])-1 and j > 0:
                if M[i][j] > M[i+1][j] and M[i][j] > M[i-1][j] and M[i][j] > M[i][j+1] and M[i][j] > M[i][j-1]:
                    res = [i, j]
                    return res

            if i == 0 and j < len(M[i])-1 and j > 0:
                if M[i][j] > M[i+1][j] and M[i][j] > M[i][j+1] and M[i][j] > M[i][j-1]:
                    res = [i, j]
                    return res

            if i == len(M)-1 and j < len(M[i])-1 and j > 0:
                if M[i][j] > M[i-1][j] and M[i][j] > M[i][j+1] and M[i][j] > M[i][j-1]:
                    res = [i, j]
                    return res

            if i > 0 and i < len(M)-1 and j == 0:
                if M[i][j] > M[i-1][j] and M[i][j] > M[i-1][j] and M[i][j] > M[i][j+1] :
                    res = [i, j]
                    return res

            if i > 0 and i < len(M)-1 and j == len(M[i])-1:
                if M[i][j] > M[i+1][j] and M[i][j] > M[i-1][j] and M[i][j] > M[i][j-1]:
                    res = [i, j]
                    return res

            if i == len(M) - 1  and j == len(M[i])-1:
                if M[i][j] > M[i-1][j] and M[i][j] > M[i][j-1]:
                    res = [i, j]
                    return res

            if i == 0 and j == len(M[i])-1:
                if M[i][j] > M[i+1][j] and M[i][j] > M[i][j-1]:
                    res = [i, j]
                    return res

            if i == 0 and j == 0:
                if M[i][j] > M[i+1][j] and M[i][j] > M[i][j+1]:
                    res = [i, j]
                    return res

            if i == len(M) - 1  and j == 0:
                if M[i][j] > M[i+1][j] and M[i][j] > M[i][j-1]:
                    res = [i, j]
                    return res

            if i == len(M) - 1  and j == len(M[i])-1:
                if M[i][j] > M[i-1][j] and M[i][j] > M[i][j-1]:
                    res = [i, j]
                    return res

    return []

arr = [[1,3,6,10,15,21,28], [2,5,9,14,20,27,34], [4,8,13,19,26,33,39],[7,12,18,25,32,38,90],[11,17,24,31,37,57,91],[99,98,97,60,59,58,56], [22,29,35,40,44,55,49]]

print(find_local_max(arr))
