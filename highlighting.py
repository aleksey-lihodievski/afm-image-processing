import cv2
import numpy as np


def calculate_z_by_x_and_y(x: int, y: int, a: int, b: int, c: int):
    return a * x + b * y + c


class Highlighting:
    @staticmethod
    def exclude_gradient(src: str, horizontal_size: int, vertical_size: int):
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"

        img = img.astype('float32')

        dst1 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=horizontal_size)
        dst2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=vertical_size)

        return img - dst1 - dst2
