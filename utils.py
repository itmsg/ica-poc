#returns a dictonary for a given array, in which each field that is not filled with 0 in the array is listed
# example: array [[-1  2][ 0 -1]] and corresponding dictonary: {(0, 0): -1, (0, 1): 2, (1, 1): -1}
def get_input_for_qbsolv(array_qubo):
    dic_qubo = {(rx, cx): c for rx, r in enumerate(array_qubo) \
                for cx, c in enumerate(r) if (c != 0.0)}
    return dic_qubo

