import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from aes_encryption.encrypt_aes_code import AES
from bwt_encryption.encrypt_bwt import improved_encrypt_bwt

class SpeedTester:    
    def __init__(self, images, encrypt_function=None, keys=None, num_rounds=None, num_iterations=10, iv=None):
        self.images = images
        self.encrypt_function = encrypt_function
        self.keys = keys
        self.num_rounds = num_rounds
        self.num_iterations = num_iterations
        self.iv = iv
    
    def aes_encrypt(self, im):
        imb = im.tobytes()
        aes = AES(self.keys, self.iv)
        encrypted_img = aes.encrypt(imb)
        return encrypted_img

    def _calculate_average_time(self, im):
        total_time = 0

        for _ in range(self.num_iterations):
            start_time = time.time()
            self.encrypt_function(im=im, keys=self.keys, num_rounds=self.num_rounds)
            total_time += time.time() - start_time

        return total_time / self.num_iterations
    
    def _calculate_average_time_aes(self, im):
        total_time = 0

        for _ in range(self.num_iterations):
            start_time = time.time()
            self.aes_encrypt(im=im)
            total_time += time.time() - start_time

        return total_time / self.num_iterations

    def run_tests(self):
        average_times = {}
        for size, im in self.images.items():
            if self.encrypt_function and not self.iv:
                avg_time = self._calculate_average_time(im)
            else:
                avg_time = self._calculate_average_time_aes(im)
            print(f"Size: {size}x{size} - Average time: {avg_time:.6f} seconds")
            average_times[size] = avg_time

        return average_times

    def plot_results(self, average_times):
        sizes = list(average_times.keys())
        times = list(average_times.values())

        plt.figure(figsize=(10, 6))
        plt.plot(sizes, times, marker='o', linestyle='-', markersize=8, color='blue')
        for size, time_value in zip(sizes, times):
            plt.text(size, time_value, f"{time_value:.3f}s", ha='center', va='bottom')
        plt.xticks(sizes)
        plt.xlabel('Image Size (pixels)')
        plt.ylabel('Average Encryption Time (seconds)')
        plt.title('Average Encryption Time by Image Size')
        plt.grid(True)
        plt.show()