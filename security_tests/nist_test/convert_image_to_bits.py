import cv2

def image_to_bits(image, output_file):
    bits = ''.join(format(byte, '08b') for byte in image.flatten())
    with open(output_file, 'w') as f:
        f.write(bits)
    print(f"Sequência de bits salva com sucesso em: {output_file}")