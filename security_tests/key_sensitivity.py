import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

def calculate_mse(imageA, imageB):
    # Verificar se as imagens têm o mesmo tamanho e são em escala de cinza
    assert imageA.shape == imageB.shape, "The images must have the same size."
    assert len(imageA.shape) == 2, "The images must be in grayscale (2 dimensions)."
    
    # Converter as imagens para float64 para maior precisão
    imageA = imageA.astype(np.float64)
    imageB = imageB.astype(np.float64)
    
    # Calcular o erro quadrático médio
    mse = np.mean((imageA - imageB) ** 2)
    return mse

def calculate_ssim(imageA, imageB):
    # Verificar se as imagens têm o mesmo tamanho
    assert imageA.shape == imageB.shape, "The images must be the same size."
    
    # Converter as imagens para um tipo suportado sem normalização
    imageA = imageA.astype(np.uint8)
    imageB = imageB.astype(np.uint8)

    # Definir o intervalo de dados de acordo com o tipo de imagem
    data_range = 255  # Para imagens de 8 bits (0-255)

    # Calcular o Structural Similarity Index
    s, _ = ssim(imageA, imageB, full=True, data_range=data_range)
    return s


def evaluate_key_sensitivity(original_image, encrypted_image, original_key, decrypt_function, num_variations=5):
    mse_values = []
    ssim_values = []
    
    def generate_key_variation(original_key, variation):
        return [num + variation * 0.000000000001 for num in original_key]

    # Gerar variações da chave e calcular MSE e SSIM
    for i in range(-num_variations // 2, num_variations // 2 + 1):
        modified_key = generate_key_variation(original_key, i)

        # Descriptografar usando a chave modificada
        decrypted_image = decrypt_function(
            im=encrypted_image,
            keys=modified_key,
            num_rounds=2
        )

        # Calcular MSE e SSIM
        mse = calculate_mse(original_image, decrypted_image)
        ssim = calculate_ssim(original_image, decrypted_image)
        mse_values.append(mse)
        ssim_values.append(ssim)

    # Gerar gráficos para visualização dos resultados
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    key_range = range(-num_variations // 2, num_variations // 2 + 1)

    axs[0].plot(key_range, mse_values, color='blue')
    axs[0].set_title("MSE Variation with Key Changes")
    axs[0].set_xlabel("Key Variation")
    axs[0].set_ylabel("Mean Squared Error (MSE)")
    axs[0].grid(True)
    axs[1].plot(key_range, ssim_values, color='blue')
    axs[1].set_title("SSIM Variation with Key Changes")
    axs[1].set_xlabel("Key Variation")
    axs[1].set_ylabel("Structural Similarity Index (SSIM)")
    axs[1].grid(True)
    plt.tight_layout()
    plt.show()