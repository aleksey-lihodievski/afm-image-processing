import cv2
import numpy as np


class SpatialFilters:
    @staticmethod
    def mean_filter(src: str, matrix_edge_size: int):
        # another name is "усреднение по окрестности"
        image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        kernel = np.ones((matrix_edge_size, matrix_edge_size), np.float32) / pow(matrix_edge_size, 2)
        mean_image = cv2.filter2D(converted_image, -1, kernel)

        return mean_image

    @staticmethod
    def edge_preserving_filter(src: str, sigma_color: float, sigma_space: float, matrix_size: int):
        image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        domain_filtered_image = cv2.bilateralFilter(converted_image, matrix_size, sigma_color, sigma_space)

        return domain_filtered_image

    @staticmethod
    def gaussian_filter(src: str, matrix_edge_size: int):
        image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        gauss = cv2.GaussianBlur(converted_image, (matrix_edge_size, matrix_edge_size), 0)

        return gauss

    @staticmethod
    def canny_edge_filter(src: str, min_treshold: float, max_treshold: float):
        image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        canny = cv2.Canny(converted_image, min_treshold, max_treshold)

        return canny