def count_sort(dictionary: list, input_list: list) -> tuple:
    res  = []

    count = [0]*len(dictionary)
    pos = [0]*len(dictionary)

    for i in range(len( input_list )):
        count[input_list[i]] += 1

    for i in range(len(count)):
        pos[i] = sum(count[:i])

    return count, pos


dictionary=[0,1,2,3,4,5,6,7,8,9,10]

input = [1,2,3,2,3,3,2,1,3,2,3,2,2]

print( count_sort(dictionary, input) )
