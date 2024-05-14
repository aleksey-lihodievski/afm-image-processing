import cv2
import numpy as np
from PySide6.QtGui import QImage


def format_image(image: cv2.typing.MatLike):
    qformat = QImage.Format.Format_Indexed8

    if len(image.shape) == 3:
        if (image.shape[2]) == 4:
            qformat = QImage.Format.Format_RGBA8888
        else:
            qformat = QImage.Format.Format_RGB888

    return QImage(image.data, image.shape[1], image.shape[0], qformat)


class FrequencyFilters:
    def __init__(self):
        print("init of frequency filters")

    @staticmethod
    def process_mean_filter(src: str):
        image = cv2.imread(src)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # TODO: add dynamic filter range (input on the screen)?
        kernel = np.ones((10, 10), np.float32) / 25
        mean_image = cv2.filter2D(converted_image, -1, kernel)

        return mean_image

    @staticmethod
    def edge_preserving_filter(src: str):
        image = cv2.imread(src)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        domain_filtered_image = cv2.edgePreservingFilter(converted_image, flags=1, sigma_s=60, sigma_r=0.6)

        return domain_filtered_image
