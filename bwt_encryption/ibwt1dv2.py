import numpy as np
def bwt1d_state_local_inverse(output_array, key, key_shift):
    size_array = output_array.shape[0]
    block_size = 8  # Tamanho do bloco
    num_blocks = size_array // block_size

    # Array de entrada
    input_array = np.zeros_like(output_array)

    # Desfaz a reorganização dos elementos do bloco
    mid = size_array // 2
    output_block = np.zeros(size_array, dtype=output_array.dtype)
    output_block[0::2] = output_array[:mid]
    output_block[1::2] = output_array[mid:]

    state = 0
    sum_shift = np.sum(output_block)
    shift = 1
    if key_shift != 0:
        shift = key_shift

    # Invert Shift - Não pode ser zero
    shift = (shift + int(sum_shift)) % 256
    output_block = np.roll(output_block, -shift)

    # Aplicação do filtro inverso em cada bloco
    for b in range(num_blocks):
        start = b * block_size
        end = start + block_size
        block = output_block[start:end].copy()
        

        # Estado local consistente com a transformada direta
        state = (key + b + state) % 256
        
        # Inversão das operações de filtro
        block[7] = np.bitwise_xor(block[7], state)
        block[7] = np.bitwise_xor(block[6], block[7])
        block[6] = np.bitwise_xor(block[6], state)
        
        block[5] = np.bitwise_xor(block[5], state)
        block[5] = np.bitwise_xor(block[4], block[5])
        block[4] = np.bitwise_xor(block[4], state)
        

        block[3] = np.bitwise_xor(block[3], state)
        block[3] = np.bitwise_xor(block[2], block[3])
        block[2] = np.bitwise_xor(block[2], state)
        

        block[1] = np.bitwise_xor(block[1], state)
        block[1] = np.bitwise_xor(block[0], block[1])
        block[0] = np.bitwise_xor(block[0], state)
        

        # Armazena o bloco no array de entrada
        input_array[start:end] = block

    return input_array

