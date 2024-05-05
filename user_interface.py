import cv2
from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QFileDialog

from frequency_filters import FrequencyFilters
from generated.main_window import Ui_MainWindow

# def open_img(self):
#     fname, filter = QFileDialog.getOpenFileName(self, 'Open File', 'C:\\Users\DELL\PycharmProjects\DemoPro',
#                                                 "Image Files (*)")
#     if fname:
#         self.loadImage(fname)
#     else:
#         print("Invalid Image")

# def save_img(self):
#     fname, filter = QFileDialog.getSaveFileName(self, 'Save File', 'C:\\', "Image Files (*.png)")
#     if fname:
#         cv2.imwrite(fname, self.image)  # Lưu trữ ảnh
#         print("Error")


class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mean_filter_button.clicked.connect(self.process)
        self.ui.upload_before_image.clicked.connect(self.load_image)

        self.ui.image_before_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ui.image_after_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.image_width = self.ui.image_before_label.width()
        self.image_height = self.ui.image_before_label.height()

        self.image_src = None

    def load_image(self):
        filename = QFileDialog.getOpenFileName()

        img = cv2.imread(filename[0])
        pixmap = QPixmap()
        pixmap.load(filename[0])

        img_width = img.shape[1]
        img_height = img.shape[0]

        label_width = self.ui.image_before_label.width()
        label_height = self.ui.image_before_label.height()

        if img_width / img_height > label_width / label_height:
            # layout by width
            self.image_width = label_width
            self.image_height = label_width / img_width * img_height
        else:
            # layout by height
            self.image_width = label_height / img_height * img_width
            self.image_height = label_height

        self.image_src = filename[0]

        self.ui.image_before_label.setPixmap(pixmap.scaled(self.image_width, self.image_height))

    def process(self):
        image = FrequencyFilters.process_mean_filter(self.image_src)

        self.print_image(image)

    def print_image(self, image: QImage):
        size = QSize(self.image_width, self.image_height)

        image = image.scaled(size, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        pixmap = QPixmap.fromImage(image)

        self.ui.image_after_label.setPixmap(pixmap)
