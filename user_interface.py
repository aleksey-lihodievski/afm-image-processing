import os
import shutil

import cv2
from PyQt6.QtCore import QDir
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QImage, QValidator, QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QFileDialog
from cv2.typing import MatLike

from flat_normalizations import FlatNormalizations
from highlighting import Highlighting
from histogram_equalizations import HistogramEqualizations
from spatial_filters import SpatialFilters
from generated.main_window import Ui_MainWindow


class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()

        int_validator = QIntValidator(1, 255, self)
        double_validator = QDoubleValidator(1, 255, 2, self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.gaussian_filter_edge_size_input.setValidator(int_validator)
        self.ui.gaussian_exclusion_edge_size_input.setValidator(int_validator)
        self.ui.mean_filter_edge_size_input.setValidator(int_validator)

        self.ui.canny_min_treshold_input.setValidator(int_validator)
        self.ui.canny_max_treshold_input.setValidator(int_validator)

        self.ui.horizontal_shadow_size_input.setValidator(int_validator)
        self.ui.vertical_shadow_size_input.setValidator(int_validator)

        self.ui.clahe_matrix_edge_size_input.setValidator(int_validator)
        self.ui.clahe_clip_limit_input.setValidator(int_validator)

        self.ui.clahe_clip_limit_input.setValidator(int_validator)

        self.ui.edge_preserving_filter_smoothing_k_input.setValidator(int_validator)
        self.ui.edge_preserving_filter_edging_k_input.setValidator(double_validator)

        self.tmp_output_file_path = 'tmp/output.jpg'
        self.tmp_applied_file_path = 'tmp/applied.jpg'

        if os.path.isdir('tmp'):
            shutil.rmtree('tmp')

        os.mkdir('tmp')

        # self.ui.mean_edge_size_input.setValidator(int_validator)

        self.ui.mean_filter_process_button.clicked.connect(self.process_mean_filter)
        self.ui.gauss_filter_process_button.clicked.connect(self.process_gaussian_blur)
        self.ui.edge_preserving_filter_process_button.clicked.connect(self.process_edge_preserving_filter)
        self.ui.gauss_flat_process_button.clicked.connect(self.process_gauss_flat)
        self.ui.canny_edge_filter_process_button.clicked.connect(self.process_canny)
        self.ui.flat_process_button.clicked.connect(self.process_points_flat)
        self.ui.clahe_process_button.clicked.connect(self.process_clahe)
        self.ui.brightness_eq_process_button.clicked.connect(self.process_brightness_eq)
        self.ui.highlighting_process_button.clicked.connect(self.process_highlighting)
        self.ui.apply_button.clicked.connect(self.apply_filter)

        self.ui.upload_before_image_button.clicked.connect(self.load_image)
        self.ui.save_after_image_button.clicked.connect(self.save_processed_image)

        self.ui.image_before_label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.ui.image_after_label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        self.image_width = round(self.ui.image_before_label.width())
        self.image_height = round(self.ui.image_after_label.height())

        self.showMaximized()
        # self.setMaximumSize(QSize(self.width(), self.height()))
        self.setFixedSize(QSize(self.width(), self.height()))

        self.update_label_sizes()

        self.image_src = None
        self.processed_image = None

        self.ui.tabWidget.setEnabled(False)

    def resizeEvent(self, event):
        self.update_label_sizes()

        QMainWindow.resizeEvent(self, event)

    def update_label_sizes(self):
        self.image_width = round(self.ui.image_before_label.width())
        self.image_height = round(self.ui.image_after_label.height())

    def load_image(self):
        filename = QFileDialog.getOpenFileName(self, "Select Image", QDir.homePath())

        self.image_src = filename[0]

        img = cv2.imread(self.image_src, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(self.tmp_output_file_path, img)

        pixmap = QPixmap()
        pixmap.load(self.tmp_output_file_path)

        img_width = img.shape[1]
        img_height = img.shape[0]

        label_width = self.ui.image_before_label.width()
        label_height = self.ui.image_before_label.height()

        if img_width / img_height > label_width / label_height:
            # layout by width
            self.image_width = round(label_width)
            self.image_height = round(label_width / img_width * img_height)
        else:
            self.image_width = round(label_height / img_height * img_width)
            self.image_height = round(label_height)

        self.ui.image_before_label.setPixmap(pixmap.scaled(self.image_width, self.image_height))
        self.ui.image_after_label.setPixmap(QPixmap())

        self.ui.tabWidget.setEnabled(True)
        self.processed_image = None

    def save_processed_image(self):
        f_name, _filter = QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath() + "/.jpg")
        if f_name:
            cv2.imwrite(f_name, self.processed_image)

    def process_mean_filter(self):
        edge_size = int(self.ui.mean_filter_edge_size_input.text())

        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = SpatialFilters.mean_filter(self.tmp_output_file_path, edge_size)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def process_gaussian_blur(self):
        edge_size = int(self.ui.gaussian_filter_edge_size_input.text())

        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = SpatialFilters.gaussian_filter(self.tmp_output_file_path, edge_size)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def process_edge_preserving_filter(self):
        smoothing = int(self.ui.edge_preserving_filter_smoothing_k_input.text())
        edging = float(self.ui.edge_preserving_filter_edging_k_input.text().replace(",", "."))

        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = SpatialFilters.edge_preserving_filter(self.tmp_output_file_path, smoothing, edging)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def process_gauss_flat(self):
        edge_size = int(self.ui.gaussian_exclusion_edge_size_input.text())

        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = FlatNormalizations.exclude_gauss(self.tmp_output_file_path, edge_size)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def process_points_flat(self):
        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = FlatNormalizations.exclude_flat(self.tmp_output_file_path)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def process_clahe(self):
        clip_limit = float(self.ui.clahe_clip_limit_input.text())
        edge_size = int(self.ui.clahe_matrix_edge_size_input.text())

        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = HistogramEqualizations.contrast_limited(self.tmp_output_file_path, clip_limit, edge_size)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def process_brightness_eq(self):
        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = HistogramEqualizations.brightness_equalizations(self.tmp_output_file_path)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def process_highlighting(self):
        horizontal = int(self.ui.horizontal_shadow_size_input.text())
        vertical = int(self.ui.vertical_shadow_size_input.text())

        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = Highlighting.exclude_gradient(self.tmp_output_file_path, horizontal, vertical)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def process_canny(self):
        min_tresh = float(self.ui.canny_min_treshold_input.text())
        max_tresh = float(self.ui.canny_max_treshold_input.text())

        print(min_tresh, max_tresh, type(min_tresh))

        QMainWindow.setCursor(self, Qt.CursorShape.WaitCursor)
        image = SpatialFilters.canny_edge_filter(self.tmp_output_file_path, min_tresh, max_tresh)
        QMainWindow.setCursor(self, Qt.CursorShape.ArrowCursor)

        self.print_image(image)

    def apply_filter(self):
        img = cv2.imread(self.tmp_applied_file_path)
        cv2.imwrite(self.tmp_output_file_path, img)
        self.ui.apply_button.setEnabled(False)

    def print_image(self, image: MatLike):
        self.processed_image = image

        # this intermediate image fixes the bug,
        # when some images appeared in qt with glitches
        cv2.imwrite(self.tmp_applied_file_path, self.processed_image)
        self.ui.apply_button.setEnabled(True)

        pixmap = QPixmap()
        pixmap.load(self.tmp_applied_file_path)

        self.ui.image_after_label.setPixmap(
            pixmap.scaled(self.image_width, self.image_height)
        )
