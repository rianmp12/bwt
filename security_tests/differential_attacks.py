import os
import cv2
import numpy as np
from PIL import Image

def uaci(original, cifrada):
    diff = np.abs(original.astype(np.int16) - cifrada.astype(np.int16))
    uaci = np.mean(diff) / 255 * 100
    return uaci

def npcr(imagem_original, imagem_modificada):
    diff = imagem_original != imagem_modificada
    npcr = np.sum(diff) / diff.size * 100
    return npcr

def uaci_npcr_metrics(original, encrypted):
    uaci_value = uaci(original, encrypted)
    npcr_value = npcr(original, encrypted)
    print(f"UACI: {uaci_value:.2f}% | NPCR: {npcr_value:.2f}%")

def process_images(directory, keys, rounds, encrypt_function, limit=None):
    uaci_list = []
    npcr_list = []
    images = []
    
    all_files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg'))]

    if limit is not None:
        all_files = all_files[:limit]

    for filename in all_files:
        img = np.array(Image.open(os.path.join(directory, filename)).convert('L'))
        images.append(img)

    for im in images:
        modified_im = im.copy()
        modified_im[0, 0] = (modified_im[0, 0] + 1) % 255

        encrypt_1 = encrypt_function(im=im, keys=keys, num_rounds=rounds)
        encrypt_2 = encrypt_function(im=modified_im, keys=keys, num_rounds=rounds)

        uaci1 = uaci(encrypt_1, encrypt_2)
        npcr1 = npcr(encrypt_1, encrypt_2)

        uaci_list.append(uaci1)
        npcr_list.append(npcr1)

    avg_uaci = np.mean(uaci_list)
    avg_npcr = np.mean(npcr_list)
    print(f"Mean UACI: {avg_uaci}\nMean NPCR: {avg_npcr}")