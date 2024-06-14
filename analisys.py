import cv2
import numpy as np
from cv2.typing import MatLike

image_names_before = [
    "afm_first_type_52.jpg",
    "afm_first_type_54.jpg",
    "afm_second_type_21.jpg",
    "afm_second_type_22.jpg",
    "bright.png",
    "intrnet_image_22_second_type.jpg",
    "intrnet_image_27_second_type.png",
    "intrnet_image_53_second_type.jpg",
    "Screenshot 2024-05-26 at 19.30.54.png",
]

image_names_after = [
    "1.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg",
    "7.jpg",
    "8.jpg",
    "9.jpg",
]

images_before_folder_path = "/Users/aleksejlihodievskij/Предметы/Диплом/Оценка/До/cropped/"

# images_after_folder_path = "/Users/aleksejlihodievskij/Предметы/Диплом/Оценка/После/ThreeDots/"
# images_after_folder_path = "/Users/aleksejlihodievskij/Предметы/Диплом/Оценка/После/Highlighting/"
images_after_folder_path = "/Users/aleksejlihodievskij/Предметы/Диплом/Оценка/После/Gaussian/"
# images_after_folder_path = "/Users/aleksejlihodievskij/Предметы/Диплом/Оценка/После/GaussianExclusion/"

# посш, ско


# СКО - Среднеквадратичная ошибка (отклонение)
def sko(before_img: MatLike, after_img: MatLike):

    before_flat = before_img.flat
    after_flat = after_img.flat

    result = float(0)

    pixels_amount = len(before_flat)

    for j in range(len(before_flat)):
        pixel_before = before_flat[j]
        pixel_after = after_flat[j]

        result += np.power(np.subtract(int(pixel_before), int(pixel_after)), 2)

    return round(result / pixels_amount, 2)

# ПОСШ - Пиковое отношение сигнал/шум
def pocsh(sko: float):
    return round(255 * np.log10(255 / sko), 2)


if __name__ == "__main__":
    for i, name in enumerate(image_names_before):
        before = cv2.imread(images_before_folder_path + name, cv2.IMREAD_GRAYSCALE)
        after = cv2.imread(images_after_folder_path + image_names_after[i], cv2.IMREAD_GRAYSCALE)

        calculated_sko = sko(before, after)
        calculated_pocsh = pocsh(calculated_sko)

        print(calculated_sko, calculated_pocsh)
