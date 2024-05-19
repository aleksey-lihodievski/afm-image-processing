import cv2
import numpy as np
# from PySide6.QtGui import QImage


# def format_image(image: cv2.typing.MatLike):
#     qformat = QImage.Format.Format_Indexed8
#
#     if len(image.shape) == 3:
#         if (image.shape[2]) == 4:
#             qformat = QImage.Format.Format_RGBA8888
#         else:
#             qformat = QImage.Format.Format_RGB888
#
#     return QImage(image.data, image.shape[1], image.shape[0], qformat)

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
    def edge_preserving_filter(src: str, smoothing: int, edging: float):
        image = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # domain_filtered_image = cv2.edgePreservingFilter(converted_image, flags=1, sigma_s=60, sigma_r=0.6)
        domain_filtered_image = cv2.edgePreservingFilter(converted_image, flags=1, sigma_s=smoothing, sigma_r=edging)

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

        # canny = cv2.Canny(converted_image, 85, 255, 3)
        canny = cv2.Canny(converted_image, min_treshold, max_treshold, 3)

        return canny
