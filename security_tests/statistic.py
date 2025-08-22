import random
from PIL import Image
import cv2
import numpy as np
from collections import Counter
import math
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def calculate_entropy(image):
    # Verifica se a imagem é colorida ou em tons de cinza
    if len(image.shape) == 3:
        # Imagem colorida
        channels = cv2.split(image)
        entropies = [calculate_entropy_single_channel(channel) for channel in channels]
        return np.mean(entropies)
    else:
        # Imagem em tons de cinza
        return calculate_entropy_single_channel(image)

def calculate_entropy_single_channel(channel):
    # Conta a frequência de cada valor de pixel no canal
    pixel_counts = Counter(channel.flatten())
    total_pixels = channel.size
    entropy = 0

    for count in pixel_counts.values():
        p_x = count / total_pixels
        entropy -= p_x * np.log2(p_x)
    
    return entropy

def plot_histogram(image, title):
    # image = cv2.imread(image_path)  
    image_array = np.array(image)

    plt.figure(figsize=(4,4))
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.hist(image_array.flatten(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.show()

def plot_histograms_together(image1, image2, title1, title2):
    image_array1 = np.array(image1)
    image_array2 = np.array(image2)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, posição 1
    plt.title(title1)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.hist(image_array1.flatten(), bins=256, range=(0, 256), color='blue', alpha=0.7)

    plt.subplot(1, 2, 2)  
    plt.title(title2)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.hist(image_array2.flatten(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.tight_layout()
    plt.show()

def calculate_and_plot_correlation(original_image, encrypted_image):
    def correlation_coefficient(x, y):
        return np.corrcoef(x.flatten(), y.flatten())[0, 1]
    
    # Coeficientes de correlação em diferentes direções
    horizontal_corr = correlation_coefficient(original_image[:, :-1], original_image[:, 1:])
    vertical_corr = correlation_coefficient(original_image[:-1, :], original_image[1:, :])
    diagonal_corr = correlation_coefficient(original_image[:-1, :-1], original_image[1:, 1:])
    encrypted_horizontal_corr = correlation_coefficient(encrypted_image[:, :-1], encrypted_image[:, 1:])
    encrypted_vertical_corr = correlation_coefficient(encrypted_image[:-1, :], encrypted_image[1:, :])
    encrypted_diagonal_corr = correlation_coefficient(encrypted_image[:-1, :-1], encrypted_image[1:, 1:])

    print("Original Image Correlation")
    print("Horizontal:", horizontal_corr)
    print("Vertical:", vertical_corr)
    print("Diagonal:", diagonal_corr)

    print("Encrypted Image Correlation")
    print("Horizontal:", encrypted_horizontal_corr)
    print("Vertical:", encrypted_vertical_corr)
    print("Diagonal:", encrypted_diagonal_corr)

def correlacao_px_adjacente(image, height, width, title):
    samples_x = []
    samples_y = []
    
    for i in range(1024):
        x = random.randint(0, height - 2)
        y = random.randint(0, width - 1)
        
        # Verificar se estamos lidando com uma imagem em escala de cinza ou uma imagem colorida
        if len(image.shape) == 2:  # Imagem em escala de cinza
            samples_x.append(image[x, y])
            samples_y.append(image[x + 1, y])
        elif len(image.shape) == 3:  # Imagem colorida
            # Se for uma imagem colorida, escolha um canal (por exemplo, canal R)
            samples_x.append(image[x, y, 0])
            samples_y.append(image[x + 1, y, 0])
        else:
            raise ValueError("Unsupported Image Format")
    
    # Converter listas para arrays numpy unidimensionais
    samples_x = np.array(samples_x).flatten()
    samples_y = np.array(samples_y).flatten()
    
    # Calcular a correlação de Pearson
    correlation, _ = pearsonr(samples_x, samples_y)
    
    # Visualização
    plt.figure(figsize=(5, 5))
    plt.scatter(samples_x, samples_y, s=2)
    plt.title(f'{title}\nCorrelation: {correlation:.4f}')
    plt.xlabel('Pixel (x, y)')
    plt.ylabel('Pixel (x+1, y)')
    plt.show()
    
    return correlation

def plot_correlacao_px_adjacente(image1, image2, height, width, title1, title2):
    samples_x1, samples_y1 = [], []
    samples_x2, samples_y2 = [], []
    
    for i in range(1024):
        x = random.randint(0, height - 2)
        y = random.randint(0, width - 1)

        # Verificar se estamos lidando com uma imagem em escala de cinza ou uma imagem colorida
        if len(image1.shape) == 2:  # Imagem em escala de cinza
            samples_x1.append(image1[x, y])
            samples_y1.append(image1[x + 1, y])
            samples_x2.append(image2[x, y])
            samples_y2.append(image2[x + 1, y])
        elif len(image1.shape) == 3:  # Imagem colorida
            # Se for uma imagem colorida, escolha um canal (por exemplo, canal R)
            samples_x1.append(image1[x, y, 0])
            samples_y1.append(image1[x + 1, y, 0])
            samples_x2.append(image2[x, y, 0])
            samples_y2.append(image2[x + 1, y, 0])
        else:
            raise ValueError("Unsupported Image Format")

    # Converter listas para arrays numpy unidimensionais
    samples_x1 = np.array(samples_x1).flatten()
    samples_y1 = np.array(samples_y1).flatten()
    samples_x2 = np.array(samples_x2).flatten()
    samples_y2 = np.array(samples_y2).flatten()

    # Calcular a correlação de Pearson para ambas as imagens
    correlation1, _ = pearsonr(samples_x1, samples_y1)
    correlation2, _ = pearsonr(samples_x2, samples_y2)

    # Visualização das correlações lado a lado
    plt.figure(figsize=(10, 5))

    # Plot da correlação da primeira imagem
    plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, posição 1
    plt.scatter(samples_x1, samples_y1, s=2)
    plt.title(f'{title1}\nCorrelation: {correlation1:.4f}')
    plt.xlabel('Pixel (x, y)')
    plt.ylabel('Pixel (x+1, y)')

    # Plot da correlação da segunda imagem
    plt.subplot(1, 2, 2)  # 1 linha, 2 colunas, posição 2
    plt.scatter(samples_x2, samples_y2, s=2)
    plt.title(f'{title2}\nCorrelation: {correlation2:.4f}')
    plt.xlabel('Pixel (x, y)')
    plt.ylabel('Pixel (x+1, y)')

    plt.tight_layout()
    plt.show()
    
    return correlation1, correlation2

def analyze_encryption_statistics(original_image, encrypted_image):
    # Calcular a entropia
    entropy = calculate_entropy(encrypted_image)
    max_entropy = 8
    entropy_percentage = (entropy / max_entropy) * 100

    print(f"Entropy of the encrypted image: {entropy:.4f} bits per pixel")
    print(f"Maximum possible entropy: {max_entropy} bits per pixel")
    print(f"Entropy percentage: {entropy_percentage:.2f}%")

    # Converter as imagens para o formato PNG
    im_png = Image.fromarray(np.uint8(original_image))
    encrypt_image_png = Image.fromarray(np.uint8(encrypted_image))

    # Exibir os histogramas lado a lado
    plot_histograms_together(
        im_png, encrypt_image_png, 
        'Original Image Histogram', 
        'Encrypted Image Histogram'
    )

    # Calcular e exibir a correlação entre as imagens
    calculate_and_plot_correlation(original_image, encrypted_image)

    # Calcular a correlação de pixels adjacentes
    height, width = original_image.shape
    correlation_original, correlation_encrypted = plot_correlacao_px_adjacente(
        original_image, encrypted_image, height, width, 
        "Adjacent Pixel Correlation - Original Image", 
        "Adjacent Pixel Correlation - Encrypted Image"
    )

    print(f"Adjacent Pixel Correlation - Original Image: {correlation_original:.4f}")
    print(f"Adjacent Pixel Correlation - Encrypted Image: {correlation_encrypted:.4f}")