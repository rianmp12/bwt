import numpy as np

def ibwt1d(input_array, diffuse=None):
    size_array = len(input_array)
    out = np.zeros(size_array, np.uint8)

    # print('type(input_array[0])')
    # print(type(input_array[0]))
    # print('type(input_array[0])')

    out[0::2] = input_array[0:size_array//2]
    out[1::2] = input_array[size_array//2:size_array]

    if diffuse is not None:
        for i in range(0, size_array, 8):
            aux = out[i]
            out[i] = np.bitwise_xor(out[i] , diffuse)

            aux2 = out[i+1]
            out[i+1] = np.bitwise_xor(aux , out[i+1])

            aux = out[i+2]
            out[i+2] = np.bitwise_xor(out[i+2] , aux2)

            aux2 = out[i+3]
            out[i+3] = np.bitwise_xor(aux , out[i+3])

            aux = out[i+4]
            out[i+4] = np.bitwise_xor(out[i+4] , aux2)

            aux2 = out[i+5]
            out[i+5] = np.bitwise_xor(aux , out[i+5])

            aux = out[i+6]
            out[i+6] = np.bitwise_xor(out[i+6] , aux2)

            out[i+7] = np.bitwise_xor(aux , out[i+7])

            diffuse = out[i+7]
    else:
        for i in range(0, size_array, 8):
            out[i+1] = np.bitwise_xor(out[i], out[i+1])
            out[i+3] = np.bitwise_xor(out[i+2], out[i+3])
            out[i+5] = np.bitwise_xor(out[i+4], out[i+5])
            out[i+7] = np.bitwise_xor(out[i+6], out[i+7])

    return out