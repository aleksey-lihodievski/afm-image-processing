import cv2
import numpy as np


def calculate_z_by_x_and_y(x: int, y: int, a: int, b: int, c: int):
    return a * x + b * y + c


class HistogramEqualizations:
    @staticmethod
    def contrast_limited(src: str, clip_limit: float, matrix_edge_size: int):
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"

        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(matrix_edge_size, matrix_edge_size))

        applied = clahe.apply(img)  # apply CLAHE to the L-channel

        return applied

    @staticmethod
    def brightness_equalizations(src: str):
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"

        minimum = np.min(img)
        maximum = np.max(img)

        for y_idx, col in enumerate(img):
            for x_idx, cell in enumerate(col):
                brightness = 255 * (img[y_idx][x_idx] - minimum) / (maximum - minimum)
                img[y_idx][x_idx] = brightness

        return img
