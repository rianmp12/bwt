import numpy as np

def chebymap(x0, k, n_samples, max_range=None):
    """
    Generate a Chebyshev sequence.

    Parameters:
    x0 (float): Initial value, must be in [-1,1]
    k (int): Chebyshev parameter, must be >= 2 for chaotic sequences
    n_samples (int): Number of samples to be generated
    max_range (int, optional): Max range for the output sequence. If None, defaults to 256.

    Returns:
    np.ndarray: Output sequence
    """
    seq = np.zeros(n_samples)
    seq_i = np.zeros(n_samples)
    seq[0] = x0
    seq_i[0] = np.arccos(-seq[0]) / np.pi

    for i in range(1, n_samples):
        seq[i] = np.cos(k * np.arccos(seq[i - 1]))
        seq_i[i] = np.arccos(-seq[i]) / np.pi
        if seq_i[i] == -1:  # Avoid disturbance effects on sequence
            seq_i[i] += 0.01

    if max_range is None:
        seq_out = np.uint8(np.mod(np.floor(seq_i * 10e14), 256))
    else:
        seq_out = np.uint32(np.mod(np.floor(seq_i * 10e14), max_range))

    return seq_out


import numpy as np
import math

def chebymap2(x0, mu, n_samples, max_range=None):
    """
    Generate a Chebyshev sequence with an improved calculation method.

    Parameters:
    x0 (float): Initial value, must be in [-1,1]
    mu (int): Chebyshev parameter, typically >= 2 for chaotic sequences
    n_samples (int): Number of samples to be generated
    max_range (int, optional): Max range for the output sequence. If None, defaults to 256.

    Returns:
    np.ndarray: Output sequence
    """
    seq = np.zeros(n_samples)
    seq_i = np.zeros(n_samples)
    seq[0] = x0
    seq_i[0] = np.arccos(-seq[0]) / np.pi

    for i in range(1, n_samples):
        Uk = seq[i - 1]
        seq[i] = math.ceil(np.cos((mu + 1) * np.arccos(Uk)) * (2**15)) - np.cos((mu + 1) * np.arccos(Uk)) * (2**15)
        seq_i[i] = np.arccos(-seq[i]) / np.pi
        if seq_i[i] == -1:  # Avoid disturbance effects on sequence
            seq_i[i] += 0.01

    if max_range is None:
        seq_out = np.uint8(np.mod(np.floor(seq_i * 10e14), 256))
    else:
        seq_out = np.uint32(np.mod(np.floor(seq_i * 10e14), max_range))

    return seq_out
