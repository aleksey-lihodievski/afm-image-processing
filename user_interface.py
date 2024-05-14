# from typing import Any

import cv2
from PyQt6.QtCore import QDir
from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QFileDialog
from cv2.typing import MatLike
# from cv2 import Mat
# from numpy import ndarray, dtype, generic

from frequency_filters import FrequencyFilters, format_image
from generated.main_window import Ui_MainWindow


class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mean_filter_process_button.clicked.connect(self.process_mean_filter)
        self.ui.edge_preserving_filter_process_button.clicked.connect(self.process_edge_preserving_filter)
        self.ui.save_after_image_button.clicked.connect(self.save_processed_image)

        self.ui.upload_before_image_button.clicked.connect(self.load_image)

        self.ui.image_before_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.ui.image_after_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter
        )

        self.image_width = round(self.ui.image_before_label.width())
        self.image_height = round(self.ui.image_after_label.height())

        self.showMaximized()
        # self.setMaximumSize(QSize(self.width(), self.height()))
        self.setFixedSize(QSize(self.width(), self.height()))

        self.update_label_sizes()

        self.image_src = None
        self.processed_image = None

    def resizeEvent(self, event):
        self.update_label_sizes()

        print("Window has been resized", event.size())
        QMainWindow.resizeEvent(self, event)

    def update_label_sizes(self):
        self.image_width = round(self.ui.image_before_label.width())
        self.image_height = round(self.ui.image_after_label.height())

    def load_image(self):
        filename = QFileDialog.getOpenFileName(self, "Select Image", QDir.homePath())

        img = cv2.imread(filename[0])
        pixmap = QPixmap()
        pixmap.load(filename[0])

        img_width = img.shape[1]
        img_height = img.shape[0]

        label_width = self.ui.image_before_label.width()
        label_height = self.ui.image_before_label.height()

        if img_width / img_height >= label_width / label_height:
            # layout by width
            self.image_width = round(label_width)
            self.image_height = round(label_width / img_width * img_height)
        else:
            print('fuck??')
            # here is the bug with glitch
            # layout by height
            # label_height -= 50

            self.image_width = round(label_height / img_height * img_width)
            self.image_height = round(label_height)

            # works without glitches ??
            # self.image_width = 500
            # self.image_height = 500

        self.image_src = filename[0]

        self.ui.image_before_label.setPixmap(pixmap.scaled(self.image_width, self.image_height))
        self.ui.image_after_label.setPixmap(QPixmap())
        self.processed_image = None

    def save_processed_image(self):
        f_name, _filter = QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath() + "/name.jpg")
        if f_name:
            cv2.imwrite(f_name, self.processed_image)

    def process_mean_filter(self):
        image = FrequencyFilters.process_mean_filter(self.image_src)

        self.print_image(image)

    def process_edge_preserving_filter(self):
        image = FrequencyFilters.edge_preserving_filter(self.image_src)

        self.print_image(image)

    def print_image(self, image: MatLike): # Mat | ndarray[Any, dtype[generic]] | ndarray
        size = QSize(self.image_width, self.image_height)
        # size = self.ui.image_before_label.size()
        # size = QSize(100, 100)

        self.processed_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # resized = cv2.resize(image, (self.image_width, self.image_height))

        # q_image = format_image(image).scaled(size)
        q_image = format_image(image) # .scaled(size)

        pixmap = QPixmap.fromImage(q_image) # .scaled(self.ui.image_before_label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        # qimage = QImage(rgb.data, rgb.shape[1], rgb.shape[0], QImage.Format_RGB888)
        # pixmap = QPixmap.fromImage(qimage)

        print(
            q_image.size(),
            self.ui.image_before_label.size(),
            self.image_width,
            self.image_height
        )
        self.ui.image_after_label.setPixmap(pixmap)
        # self.ui.image_after_label.setPixmap(self.ui.image_before_label.pixmap())
