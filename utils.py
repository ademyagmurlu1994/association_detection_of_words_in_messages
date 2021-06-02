import numpy as np
import combination

def get_distinct_value_array(matrix):
    distinct_array = []
    for row in matrix:
        for item in row:
            if (item in distinct_array) == False:
                distinct_array.append(item)

    return distinct_array

def get_frekans_subarray(matrix, sub_array):
    count = 0
    for item in matrix:
        flag = False
        for sub_item in sub_array:
            if sub_item in item:
                flag = True
            else:
                flag = False
                break

        if flag:
            count += 1
    return count


def get_association_table(matrix_message_word, minimum_frekans):
    L = []
    frekans_array = []
    temp_L = matrix_message_word
    temp_frekans_array = []
    index = 1

    while(True):
        distinct_array = get_distinct_value_array(temp_L)
        cmb = combination.find_combination(distinct_array, len(distinct_array), index)
        temp_L = []
        stop_counter = 0

        for sub_array in cmb:
            if get_frekans_subarray(matrix_message_word, sub_array) >= minimum_frekans:
                temp_L.append(sub_array)
                temp_frekans_array.append(get_frekans_subarray(matrix_message_word, sub_array))
            else:
                stop_counter += 1

            if stop_counter == len(cmb):
                return L, frekans_array

        frekans_array = temp_frekans_array
        L = temp_L

        cmb.clear()
        temp_frekans_array = []
        index += 1


def make_message_fit(messages):
    messages_word = []
    for msg in messages:
        messages_word.append(msg.split(' '))

    return messages_word

