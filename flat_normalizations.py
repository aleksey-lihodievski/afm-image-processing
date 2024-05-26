import cv2
import numpy as np


def calculate_z_by_x_and_y(x: int, y: int, a: float, b: float, c: float):
    return a * x + b * y + c


class FlatNormalizations:
    @staticmethod
    def exclude_flat(src: str):
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"

        img = img.astype('int16')

        # z = ax + by + c
        # where z is height and c is min height

        top_left = img[0][0]
        top_right = img[0][-1]
        bottom_left = img[-1][0]
        bottom_right = img[-1][-1]

        plane_matrix = np.array([
            [0., 0, 1],
            [0., len(img), 1],
            [len(img[0]), 0, 1]
            # [len(img), len(img[0]), 1]
        ])  # Матрица (левая часть системы)
        perp_vector = np.array([top_left, bottom_left, top_right])  # Вектор (правая часть системы)

        flat_coefs = np.linalg.solve(plane_matrix, perp_vector)

        a = flat_coefs[0]  # for x
        b = flat_coefs[1]  # for y
        c = flat_coefs[2]  #

        for y_idx, col in enumerate(img):
            for x_idx, cell in enumerate(col):
                img[y_idx][x_idx] -= calculate_z_by_x_and_y(x_idx, y_idx, float(a), float(b), float(c))

        img = np.add(img, abs(np.min(img)))

        coef = 255 / np.max(img)

        img = np.multiply(img, coef)
        img = img.astype('uint8')

        return img

    @staticmethod
    def exclude_gauss(src: str, matrix_edge_size: int):
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"

        gauss = cv2.GaussianBlur(img, (matrix_edge_size, matrix_edge_size), 0)

        # cv2.imwrite('normal??.jpg', gauss - img)

        return gauss - img
