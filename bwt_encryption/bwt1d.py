import numpy as np

def bwt1d(input_array, diffuse=None):
    size_array = input_array.shape[0]
    if diffuse is not None:
        for i in range(0, size_array, 8):
            # Filtro Grupo 1
            input_array[i] = np.bitwise_xor(input_array[i], diffuse)
            input_array[i+1] = np.bitwise_xor(input_array[i], input_array[i+1])

            input_array[i+2] = np.bitwise_xor(input_array[i+1], input_array[i+2])
            input_array[i+3] = np.bitwise_xor(input_array[i+2], input_array[i+3])

            input_array[i+4] = np.bitwise_xor(input_array[i+3], input_array[i+4])
            input_array[i+5] = np.bitwise_xor(input_array[i+4], input_array[i+5])

            input_array[i+6] = np.bitwise_xor(input_array[i+5], input_array[i+6])
            input_array[i+7] = np.bitwise_xor(input_array[i+6], input_array[i+7])

            diffuse = input_array[i+7]

    else:
        for i in range(0, size_array, 8):
            # Filtro Grupo 1
            input_array[i+1] = np.bitwise_xor(input_array[i], input_array[i+1])
            input_array[i+3] = np.bitwise_xor(input_array[i+2], input_array[i+3])
            input_array[i+5] = np.bitwise_xor(input_array[i+4], input_array[i+5])
            input_array[i+7] = np.bitwise_xor(input_array[i+6], input_array[i+7])

    output_array = np.concatenate([input_array[0::2], input_array[1::2]])
    return output_array