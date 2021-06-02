combination_array = []

def find_combination(input_array, n, r):
    temp_array = [0] * r
    combination_main(input_array, temp_array, 0,
                         n - 1, 0, r)
    return combination_array


def combination_main(input_array, temp_array, start,
                    end, index, r):
    if (index == r):
        temp = temp_array[:]  # make unrefere variable
        combination_array.append(temp)
        return
    index = start
    while (index <= end and end - index + 1 >= r - index):
        temp_array[index] = input_array[index]
        combination_main(input_array, temp_array, index + 1,
                             end, index + 1, r)
        index += 1