import cv2
import numpy as np


def calculate_z_by_x_and_y(x: int, y: int, a: float, b: float, c: float):
    return a * x + b * y + c


class FlatNormalizations:
    @staticmethod
    def exclude_flat(src: str):
        print('flat??')
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"

        img = img.astype('int16')

        # z = ax + by + c
        # where z is height and c is min height (maybe)
        # this shit can produce gradients with certain angle

        top_left = img[0][0]
        top_right = img[0][-1]
        bottom_left = img[-1][0]
        bottom_right = img[-1][-1]

        # https://xn--80ahcjeib4ac4d.xn--p1ai/information/solving_systems_of_linear_equations_in_python/#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80-5.-%D0%9D%D0%B0%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D0%BB%D0%BE%D1%81%D0%BA%D0%BE%D1%81%D1%82%D0%B8-%D0%BF%D0%BE-%D1%82%D0%BE%D1%87%D0%BA%D0%B0%D0%BC,-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5-%D0%BE%D0%BD%D0%B0-%D0%BF%D1%80%D0%BE%D1%85%D0%BE%D0%B4%D0%B8%D1%82.
        # TODO: make flattening using three points and then do it again with other three points including another corner
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
