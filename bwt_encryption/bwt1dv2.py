import numpy as np


def bwt1d_state_local(input_array, key, key_shift):
    size_array = input_array.shape[0]
    block_size = 8  # Tamanho do bloco
    num_blocks = size_array // block_size

    # Array de saída
    output_array = np.zeros_like(input_array)
    state = 0
    

    # Aplicação do filtro de grupo em cada bloco
    for b in range(num_blocks):
        start = b * block_size
        end = start + block_size
        block = input_array[start:end].copy()
        
        # Estado local independente dos dados do bloco
        state = (key + b + state) % 256

        # Aplicação do filtro de grupo 1 dependente do estado local
        block[0] = np.bitwise_xor(block[0], state)
        block[1] = np.bitwise_xor(block[0], block[1])
        block[1] = np.bitwise_xor(block[1], state)

        block[2] = np.bitwise_xor(block[2], state)
        block[3] = np.bitwise_xor(block[2], block[3])
        block[3] = np.bitwise_xor(block[3], state)
        
        block[4] = np.bitwise_xor(block[4], state)
        block[5] = np.bitwise_xor(block[4], block[5])
        block[5] = np.bitwise_xor(block[5], state)
        
        block[6] = np.bitwise_xor(block[6], state)
        block[7] = np.bitwise_xor(block[6], block[7])
        block[7] = np.bitwise_xor(block[7], state)

        # Armazena o bloco reorganizado no array de saída
        output_array[start:end] = block
    
    shift = 1
    if key_shift != 0:
        shift = key_shift

    sum_shift = np.sum(output_array)
    # Shift array - Não pode ser zero
    shift = (shift + int(sum_shift)) % 256
    output_array = np.roll(output_array, shift)

    # Reorganização dos elementos do bloco
    output_block = np.concatenate([output_array[0::2], output_array[1::2]])

    


    return output_block

