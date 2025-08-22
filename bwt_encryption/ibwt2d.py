import numpy as np
from bwt_encryption.ibwt1dv2 import bwt1d_state_local_inverse
from bwt_encryption.chebyshev import chebymap2


def ibwt2d(matrix, first_x0, first_k, level=1):
    if level not in [1, 2, 3, 4]:
        raise ValueError("level must be either 1, 2, 3, or 4")

    size_m = matrix.shape

    #Generate random keys
    keys_i = chebymap2(first_x0, first_k, size_m[0], 255).tolist()
    keys_j = keys_i[::-1]

    matrix_out = np.copy(matrix)
    for k in range(level, 0, -1):
        # print("k", k)
        split_size_i = matrix_out.shape[0] // (2 ** (k - 1))
        split_size_j = matrix_out.shape[1] // (2 ** (k - 1))
        pad_i = split_size_i % 8
        pad_j = split_size_j % 8

        for j in range(split_size_j + pad_j):
            matrix_out[0:split_size_i+pad_i, j] = bwt1d_state_local_inverse(matrix_out[0:split_size_i+pad_i, j].T, keys_j[j]).T

        for i in range(split_size_i + pad_i):
            matrix_out[i, 0:split_size_j+pad_j] = bwt1d_state_local_inverse(matrix_out[i, 0:split_size_j+pad_j], keys_i[i])

    return matrix_out