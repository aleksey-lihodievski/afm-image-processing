# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2560, 1313)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet(u"QLabel {\n"
"	border: 1px solid white;\n"
"	width: 50%;\n"
"}")
        self.groupBox_3.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.image_before_label = QLabel(self.groupBox_3)
        self.image_before_label.setObjectName(u"image_before_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_before_label.sizePolicy().hasHeightForWidth())
        self.image_before_label.setSizePolicy(sizePolicy1)
        self.image_before_label.setStyleSheet(u"")
        self.image_before_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.image_before_label)

        self.image_after_label = QLabel(self.groupBox_3)
        self.image_after_label.setObjectName(u"image_after_label")
        sizePolicy1.setHeightForWidth(self.image_after_label.sizePolicy().hasHeightForWidth())
        self.image_after_label.setSizePolicy(sizePolicy1)
        self.image_after_label.setStyleSheet(u"")
        self.image_after_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.image_after_label)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(True)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.upload_before_image_button = QPushButton(self.groupBox)
        self.upload_before_image_button.setObjectName(u"upload_before_image_button")
        self.upload_before_image_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.upload_before_image_button.sizePolicy().hasHeightForWidth())
        self.upload_before_image_button.setSizePolicy(sizePolicy2)
        self.upload_before_image_button.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.upload_before_image_button)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(True)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.apply_button = QPushButton(self.groupBox_2)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setEnabled(False)
        self.apply_button.setCheckable(False)
        self.apply_button.setChecked(False)

        self.horizontalLayout_3.addWidget(self.apply_button)

        self.save_after_image_button = QPushButton(self.groupBox_2)
        self.save_after_image_button.setObjectName(u"save_after_image_button")
        self.save_after_image_button.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.save_after_image_button.sizePolicy().hasHeightForWidth())
        self.save_after_image_button.setSizePolicy(sizePolicy2)
        self.save_after_image_button.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.save_after_image_button.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.save_after_image_button)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setDocumentMode(True)
        self.gaussian_filter = QWidget()
        self.gaussian_filter.setObjectName(u"gaussian_filter")
        self.verticalLayout_3 = QVBoxLayout(self.gaussian_filter)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_14 = QLabel(self.gaussian_filter)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_3.addWidget(self.label_14)

        self.groupBox_5 = QGroupBox(self.gaussian_filter)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy4)
        self.groupBox_5.setFlat(False)
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.groupBox_19 = QGroupBox(self.groupBox_5)
        self.groupBox_19.setObjectName(u"groupBox_19")
        sizePolicy4.setHeightForWidth(self.groupBox_19.sizePolicy().hasHeightForWidth())
        self.groupBox_19.setSizePolicy(sizePolicy4)
        self.groupBox_19.setFlat(True)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.groupBox_19)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.verticalLayout_18.addWidget(self.label_9)

        self.gaussian_filter_edge_size_input = QLineEdit(self.groupBox_19)
        self.gaussian_filter_edge_size_input.setObjectName(u"gaussian_filter_edge_size_input")

        self.verticalLayout_18.addWidget(self.gaussian_filter_edge_size_input)


        self.verticalLayout_26.addWidget(self.groupBox_19)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.gauss_filter_process_button = QPushButton(self.gaussian_filter)
        self.gauss_filter_process_button.setObjectName(u"gauss_filter_process_button")
        sizePolicy4.setHeightForWidth(self.gauss_filter_process_button.sizePolicy().hasHeightForWidth())
        self.gauss_filter_process_button.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.gauss_filter_process_button)

        self.tabWidget.addTab(self.gaussian_filter, "")
        self.mean_filter = QWidget()
        self.mean_filter.setObjectName(u"mean_filter")
        self.verticalLayout = QVBoxLayout(self.mean_filter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_24 = QGroupBox(self.mean_filter)
        self.groupBox_24.setObjectName(u"groupBox_24")
        sizePolicy4.setHeightForWidth(self.groupBox_24.sizePolicy().hasHeightForWidth())
        self.groupBox_24.setSizePolicy(sizePolicy4)
        self.groupBox_24.setFlat(False)
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_24)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.groupBox_21 = QGroupBox(self.groupBox_24)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy4.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy4)
        self.groupBox_21.setFlat(True)
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.groupBox_21)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)

        self.verticalLayout_19.addWidget(self.label_10)

        self.mean_filter_edge_size_input = QLineEdit(self.groupBox_21)
        self.mean_filter_edge_size_input.setObjectName(u"mean_filter_edge_size_input")

        self.verticalLayout_19.addWidget(self.mean_filter_edge_size_input)


        self.verticalLayout_25.addWidget(self.groupBox_21)


        self.verticalLayout.addWidget(self.groupBox_24)

        self.mean_filter_process_button = QPushButton(self.mean_filter)
        self.mean_filter_process_button.setObjectName(u"mean_filter_process_button")
        sizePolicy4.setHeightForWidth(self.mean_filter_process_button.sizePolicy().hasHeightForWidth())
        self.mean_filter_process_button.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.mean_filter_process_button)

        self.tabWidget.addTab(self.mean_filter, "")
        self.edge_preserving = QWidget()
        self.edge_preserving.setObjectName(u"edge_preserving")
        self.verticalLayout_4 = QVBoxLayout(self.edge_preserving)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_25 = QGroupBox(self.edge_preserving)
        self.groupBox_25.setObjectName(u"groupBox_25")
        sizePolicy4.setHeightForWidth(self.groupBox_25.sizePolicy().hasHeightForWidth())
        self.groupBox_25.setSizePolicy(sizePolicy4)
        self.groupBox_25.setFlat(False)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_23 = QGroupBox(self.groupBox_25)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy4.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy4)
        self.groupBox_23.setFlat(True)
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.groupBox_23)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)

        self.verticalLayout_23.addWidget(self.label_11)

        self.edge_preserving_filter_smoothing_k_input = QLineEdit(self.groupBox_23)
        self.edge_preserving_filter_smoothing_k_input.setObjectName(u"edge_preserving_filter_smoothing_k_input")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.edge_preserving_filter_smoothing_k_input.sizePolicy().hasHeightForWidth())
        self.edge_preserving_filter_smoothing_k_input.setSizePolicy(sizePolicy5)

        self.verticalLayout_23.addWidget(self.edge_preserving_filter_smoothing_k_input)


        self.horizontalLayout_7.addWidget(self.groupBox_23)

        self.groupBox_7 = QGroupBox(self.groupBox_25)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFlat(True)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_21.addWidget(self.label_16)

        self.edge_preserving_filter_edging_k_input = QLineEdit(self.groupBox_7)
        self.edge_preserving_filter_edging_k_input.setObjectName(u"edge_preserving_filter_edging_k_input")

        self.verticalLayout_21.addWidget(self.edge_preserving_filter_edging_k_input)


        self.horizontalLayout_7.addWidget(self.groupBox_7)


        self.verticalLayout_4.addWidget(self.groupBox_25)

        self.edge_preserving_filter_process_button = QPushButton(self.edge_preserving)
        self.edge_preserving_filter_process_button.setObjectName(u"edge_preserving_filter_process_button")
        sizePolicy4.setHeightForWidth(self.edge_preserving_filter_process_button.sizePolicy().hasHeightForWidth())
        self.edge_preserving_filter_process_button.setSizePolicy(sizePolicy4)

        self.verticalLayout_4.addWidget(self.edge_preserving_filter_process_button)

        self.tabWidget.addTab(self.edge_preserving, "")
        self.gauss_exclusion = QWidget()
        self.gauss_exclusion.setObjectName(u"gauss_exclusion")
        self.verticalLayout_5 = QVBoxLayout(self.gauss_exclusion)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_15 = QLabel(self.gauss_exclusion)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_5.addWidget(self.label_15)

        self.groupBox_6 = QGroupBox(self.gauss_exclusion)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy4.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy4)
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.groupBox_27 = QGroupBox(self.groupBox_6)
        self.groupBox_27.setObjectName(u"groupBox_27")
        sizePolicy4.setHeightForWidth(self.groupBox_27.sizePolicy().hasHeightForWidth())
        self.groupBox_27.setSizePolicy(sizePolicy4)
        self.groupBox_27.setFlat(True)
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_27)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.groupBox_27)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)

        self.verticalLayout_29.addWidget(self.label_12)

        self.gaussian_exclusion_edge_size_input = QLineEdit(self.groupBox_27)
        self.gaussian_exclusion_edge_size_input.setObjectName(u"gaussian_exclusion_edge_size_input")

        self.verticalLayout_29.addWidget(self.gaussian_exclusion_edge_size_input)


        self.verticalLayout_20.addWidget(self.groupBox_27)


        self.verticalLayout_5.addWidget(self.groupBox_6)

        self.gauss_flat_process_button = QPushButton(self.gauss_exclusion)
        self.gauss_flat_process_button.setObjectName(u"gauss_flat_process_button")
        sizePolicy5.setHeightForWidth(self.gauss_flat_process_button.sizePolicy().hasHeightForWidth())
        self.gauss_flat_process_button.setSizePolicy(sizePolicy5)

        self.verticalLayout_5.addWidget(self.gauss_flat_process_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.tabWidget.addTab(self.gauss_exclusion, "")
        self.flat_exclusion = QWidget()
        self.flat_exclusion.setObjectName(u"flat_exclusion")
        self.verticalLayout_9 = QVBoxLayout(self.flat_exclusion)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.flat_exclusion)
        self.label_13.setObjectName(u"label_13")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy6)

        self.verticalLayout_9.addWidget(self.label_13)

        self.flat_process_button = QPushButton(self.flat_exclusion)
        self.flat_process_button.setObjectName(u"flat_process_button")
        sizePolicy5.setHeightForWidth(self.flat_process_button.sizePolicy().hasHeightForWidth())
        self.flat_process_button.setSizePolicy(sizePolicy5)

        self.verticalLayout_9.addWidget(self.flat_process_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.tabWidget.addTab(self.flat_exclusion, "")
        self.brightness_equalization = QWidget()
        self.brightness_equalization.setObjectName(u"brightness_equalization")
        self.verticalLayout_6 = QVBoxLayout(self.brightness_equalization)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.brightness_equalization)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.label_8)

        self.brightness_eq_process_button = QPushButton(self.brightness_equalization)
        self.brightness_eq_process_button.setObjectName(u"brightness_eq_process_button")
        sizePolicy5.setHeightForWidth(self.brightness_eq_process_button.sizePolicy().hasHeightForWidth())
        self.brightness_eq_process_button.setSizePolicy(sizePolicy5)

        self.verticalLayout_6.addWidget(self.brightness_eq_process_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.tabWidget.addTab(self.brightness_equalization, "")
        self.clahe = QWidget()
        self.clahe.setObjectName(u"clahe")
        self.verticalLayout_7 = QVBoxLayout(self.clahe)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_10 = QGroupBox(self.clahe)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy6.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy6)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_17 = QGroupBox(self.groupBox_10)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy7)
        self.groupBox_17.setFlat(True)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.groupBox_17)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_16.addWidget(self.label_6)

        self.clahe_clip_limit_input = QLineEdit(self.groupBox_17)
        self.clahe_clip_limit_input.setObjectName(u"clahe_clip_limit_input")

        self.verticalLayout_16.addWidget(self.clahe_clip_limit_input)


        self.horizontalLayout_6.addWidget(self.groupBox_17)

        self.groupBox_18 = QGroupBox(self.groupBox_10)
        self.groupBox_18.setObjectName(u"groupBox_18")
        sizePolicy7.setHeightForWidth(self.groupBox_18.sizePolicy().hasHeightForWidth())
        self.groupBox_18.setSizePolicy(sizePolicy7)
        self.groupBox_18.setFlat(True)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.groupBox_18)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_17.addWidget(self.label_7)

        self.clahe_matrix_edge_size_input = QLineEdit(self.groupBox_18)
        self.clahe_matrix_edge_size_input.setObjectName(u"clahe_matrix_edge_size_input")

        self.verticalLayout_17.addWidget(self.clahe_matrix_edge_size_input)


        self.horizontalLayout_6.addWidget(self.groupBox_18)


        self.verticalLayout_7.addWidget(self.groupBox_10, 0, Qt.AlignmentFlag.AlignLeft)

        self.clahe_process_button = QPushButton(self.clahe)
        self.clahe_process_button.setObjectName(u"clahe_process_button")
        sizePolicy5.setHeightForWidth(self.clahe_process_button.sizePolicy().hasHeightForWidth())
        self.clahe_process_button.setSizePolicy(sizePolicy5)

        self.verticalLayout_7.addWidget(self.clahe_process_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.tabWidget.addTab(self.clahe, "")
        self.highlighting = QWidget()
        self.highlighting.setObjectName(u"highlighting")
        self.verticalLayout_8 = QVBoxLayout(self.highlighting)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_11 = QGroupBox(self.highlighting)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFlat(True)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.groupBox_11)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_13.addWidget(self.label_3)

        self.groupBox_14 = QGroupBox(self.groupBox_11)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy7.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy7)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_15 = QGroupBox(self.groupBox_14)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setFlat(True)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_15)
#ifndef Q_OS_MAC
        self.verticalLayout_15.setSpacing(-1)
#endif
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.groupBox_15)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_15.addWidget(self.label_4)

        self.horizontal_shadow_size_input = QLineEdit(self.groupBox_15)
        self.horizontal_shadow_size_input.setObjectName(u"horizontal_shadow_size_input")

        self.verticalLayout_15.addWidget(self.horizontal_shadow_size_input)


        self.horizontalLayout_5.addWidget(self.groupBox_15)

        self.groupBox_16 = QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setFlat(True)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_16)
#ifndef Q_OS_MAC
        self.verticalLayout_14.setSpacing(-1)
#endif
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.groupBox_16)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_14.addWidget(self.label_5)

        self.vertical_shadow_size_input = QLineEdit(self.groupBox_16)
        self.vertical_shadow_size_input.setObjectName(u"vertical_shadow_size_input")

        self.verticalLayout_14.addWidget(self.vertical_shadow_size_input)


        self.horizontalLayout_5.addWidget(self.groupBox_16)


        self.verticalLayout_13.addWidget(self.groupBox_14)


        self.verticalLayout_8.addWidget(self.groupBox_11)

        self.highlighting_process_button = QPushButton(self.highlighting)
        self.highlighting_process_button.setObjectName(u"highlighting_process_button")
        sizePolicy5.setHeightForWidth(self.highlighting_process_button.sizePolicy().hasHeightForWidth())
        self.highlighting_process_button.setSizePolicy(sizePolicy5)

        self.verticalLayout_8.addWidget(self.highlighting_process_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.tabWidget.addTab(self.highlighting, "")
        self.canny_edge_filter = QWidget()
        self.canny_edge_filter.setObjectName(u"canny_edge_filter")
        self.verticalLayout_10 = QVBoxLayout(self.canny_edge_filter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_4 = QGroupBox(self.canny_edge_filter)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy4.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy4)
        self.groupBox_4.setFlat(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_12 = QGroupBox(self.groupBox_4)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(109, 0))
        self.groupBox_12.setFlat(True)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.groupBox_12)
        self.label.setObjectName(u"label")

        self.verticalLayout_12.addWidget(self.label)

        self.canny_min_treshold_input = QLineEdit(self.groupBox_12)
        self.canny_min_treshold_input.setObjectName(u"canny_min_treshold_input")

        self.verticalLayout_12.addWidget(self.canny_min_treshold_input)


        self.horizontalLayout_4.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.groupBox_4)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy8)
        self.groupBox_13.setFlat(True)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.groupBox_13)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2)

        self.canny_max_treshold_input = QLineEdit(self.groupBox_13)
        self.canny_max_treshold_input.setObjectName(u"canny_max_treshold_input")

        self.verticalLayout_11.addWidget(self.canny_max_treshold_input)


        self.horizontalLayout_4.addWidget(self.groupBox_13)


        self.verticalLayout_10.addWidget(self.groupBox_4)

        self.canny_edge_filter_process_button = QPushButton(self.canny_edge_filter)
        self.canny_edge_filter_process_button.setObjectName(u"canny_edge_filter_process_button")

        self.verticalLayout_10.addWidget(self.canny_edge_filter_process_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.tabWidget.addTab(self.canny_edge_filter, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AFM processing", None))
        self.groupBox_3.setTitle("")
        self.image_before_label.setText("")
        self.image_after_label.setText("")
        self.groupBox.setTitle("")
        self.upload_before_image_button.setText(QCoreApplication.translate("MainWindow", u"Upload image", None))
        self.groupBox_2.setTitle("")
        self.apply_button.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.save_after_image_button.setText(QCoreApplication.translate("MainWindow", u"Save image", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Edge Size should only be even due to algorithm speciefics", None))
        self.groupBox_5.setTitle("")
        self.groupBox_19.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Matrix Edge Size", None))
        self.gaussian_filter_edge_size_input.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.gauss_filter_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gaussian_filter), QCoreApplication.translate("MainWindow", u"Gaussian filter", None))
        self.groupBox_24.setTitle("")
        self.groupBox_21.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Matrix Edge Size", None))
        self.mean_filter_edge_size_input.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.mean_filter_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mean_filter), QCoreApplication.translate("MainWindow", u"Mean filter", None))
        self.groupBox_25.setTitle("")
        self.groupBox_23.setTitle("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Smoothing", None))
        self.edge_preserving_filter_smoothing_k_input.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.groupBox_7.setTitle("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Edge Preserving (0-1)", None))
        self.edge_preserving_filter_edging_k_input.setText(QCoreApplication.translate("MainWindow", u"0,15", None))
        self.edge_preserving_filter_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.edge_preserving), QCoreApplication.translate("MainWindow", u"Edge preserving", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Edge Size should only be even due to algorithm speciefics", None))
        self.groupBox_6.setTitle("")
        self.groupBox_27.setTitle("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Matrix Edge Size", None))
        self.gaussian_exclusion_edge_size_input.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.gauss_flat_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gauss_exclusion), QCoreApplication.translate("MainWindow", u"Gauss Exclusion", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"This method takes three dots (both top and left bottom), and levels plane built by using them.", None))
        self.flat_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.flat_exclusion), QCoreApplication.translate("MainWindow", u"Flat Exclusion", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"This method has no argument due to it's simplicity", None))
        self.brightness_eq_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.brightness_equalization), QCoreApplication.translate("MainWindow", u"Brightness Equalization", None))
        self.groupBox_10.setTitle("")
        self.groupBox_17.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Clip limit", None))
        self.clahe_clip_limit_input.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.groupBox_18.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Matrix Edge Size", None))
        self.clahe_matrix_edge_size_input.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.clahe_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clahe), QCoreApplication.translate("MainWindow", u"CLAHE", None))
        self.groupBox_11.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Shadow Sizes should be even and less than or equal 31", None))
        self.groupBox_14.setTitle("")
        self.groupBox_15.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Horizontal shadow", None))
        self.horizontal_shadow_size_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.groupBox_16.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Vertical shadow", None))
        self.vertical_shadow_size_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.highlighting_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.highlighting), QCoreApplication.translate("MainWindow", u"Highlighting", None))
        self.groupBox_4.setTitle("")
        self.groupBox_12.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Min Treshold", None))
        self.canny_min_treshold_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_13.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max Treshold", None))
        self.canny_max_treshold_input.setText(QCoreApplication.translate("MainWindow", u"255", None))
        self.canny_edge_filter_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canny_edge_filter), QCoreApplication.translate("MainWindow", u"Canny Edge Filter", None))
    # retranslateUi

