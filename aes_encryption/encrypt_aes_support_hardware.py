from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def encrypt_aes(image_path, key):
    # Certifique-se de que a chave é de 16, 24 ou 32 bytes (128, 192 ou 256 bits)
    if isinstance(key, int):
        # Converter o número inteiro em bytes (16 bytes = 128 bits)
        key = key.to_bytes(16, 'big')

    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=default_backend())
    encryptor = cipher.encryptor()

    # Abrir a imagem e converter para bytes
    image = Image.open(image_path).convert('L')  # Convertendo a imagem para escala de cinza
    image_array = np.array(image)
    image_bytes = image_array.tobytes()

    # Criptografar os dados da imagem
    encrypted_data = encryptor.update(image_bytes) + encryptor.finalize()

    # Converter os bytes criptografados de volta para uma matriz NumPy
    encrypted_image_array = np.frombuffer(encrypted_data, dtype=np.uint8).reshape(image_array.shape)

    return encrypted_image_array


def decrypt_aes(encrypted_data, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Use PKCS7 unpadding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data