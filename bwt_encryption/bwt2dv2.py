import numpy as np
from bwt_encryption.bwt1dv2 import bwt1d_state_local
from bwt_encryption.chebyshev import chebymap2

def bwt2dv2(im, keys, num_rounds=2):

    # Error checks
    if len(im.shape) != 2:
        raise ValueError("Input im must be 2D")

    if num_rounds not in [1, 2, 3, 4]:
        raise ValueError("num_rounds must be either 1, 2, 3, or 4 if it is supplied")

    # Size of block that will be processed by bwt1d.
    # TODO: Must be configurable on bwt1d and here.
    blocksize = 8

    size_m = im.shape
    # print("size_m", size_m)
    matrix_out = np.copy(im)

    #Generate random keys
    keys_i = chebymap2(keys[0], keys[1], size_m[0], 255).tolist()
    keys_j = keys_i[::-1]
    keys_i_shift = chebymap2(keys[2], keys[3], size_m[0], 255).tolist()
    keys_j_shift = keys_i_shift[::-1]

    for k in range(num_rounds):
        # TODO: Fix split_size to each dimension
        split_size_i = size_m[0] // (2 ** k)
        split_size_j = size_m[1] // (2 ** k)

        pad_i = split_size_i % blocksize
        pad_j = split_size_j % blocksize
        
        for i in range(split_size_i + pad_i):
            matrix_out[i, :split_size_j + pad_j] = bwt1d_state_local(matrix_out[i, :split_size_j + pad_j], keys_i[i], keys_i_shift[i])

        for j in range(split_size_j + pad_j):
            matrix_out[:split_size_i + pad_i, j] = bwt1d_state_local(matrix_out[:split_size_i + pad_i, j].T, keys_j[j], keys_j_shift[j]).T
    
    return matrix_out

# You'll need to implement the bwt1d function separately.
# Make sure it works with NumPy arrays for the above code to work correctly.