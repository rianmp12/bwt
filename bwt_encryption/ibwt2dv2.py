import numpy as np
from bwt_encryption.ibwt1dv2 import bwt1d_state_local_inverse
from bwt_encryption.chebyshev import chebymap2


def ibwt2dv2(im, keys, num_rounds=2):
    if num_rounds not in [1, 2, 3, 4]:
        raise ValueError("num_rounds must be either 1, 2, 3, or 4")

    size_m = im.shape

    # Generate random keys
    keys_i = chebymap2(keys[0], keys[1], size_m[0], 255).tolist()
    keys_j = keys_i[::-1]
    keys_i_shift = chebymap2(keys[2], keys[3], size_m[0], 255).tolist()
    keys_j_shift = keys_i_shift[::-1]

    matrix_out = np.copy(im)
    for k in range(num_rounds, 0, -1):
        split_size_i = matrix_out.shape[0] // (2 ** (k - 1))
        split_size_j = matrix_out.shape[1] // (2 ** (k - 1))
        pad_i = split_size_i % 8
        pad_j = split_size_j % 8

        for j in range(split_size_j + pad_j):
            matrix_out[0:split_size_i+pad_i, j] = bwt1d_state_local_inverse(matrix_out[0:split_size_i+pad_i, j].T, keys_j[j], keys_j_shift[j]).T

        for i in range(split_size_i + pad_i):
            matrix_out[i, 0:split_size_j+pad_j] = bwt1d_state_local_inverse(matrix_out[i, 0:split_size_j+pad_j], keys_i[i], keys_i_shift[i])

    return matrix_out