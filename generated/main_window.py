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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(592, 479)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet(u"QLabel {\n"
"	border: 1px solid white;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.image_before_label = QLabel(self.groupBox_3)
        self.image_before_label.setObjectName(u"image_before_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
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

        self.upload_before_image_button = QPushButton(self.centralwidget)
        self.upload_before_image_button.setObjectName(u"upload_before_image_button")
        self.upload_before_image_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.upload_before_image_button.sizePolicy().hasHeightForWidth())
        self.upload_before_image_button.setSizePolicy(sizePolicy2)
        self.upload_before_image_button.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.upload_before_image_button.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.upload_before_image_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setDocumentMode(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout = QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mean_filter_process_button = QPushButton(self.tab_1)
        self.mean_filter_process_button.setObjectName(u"mean_filter_process_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mean_filter_process_button.sizePolicy().hasHeightForWidth())
        self.mean_filter_process_button.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.mean_filter_process_button)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.edge_preserving_filter_process_button = QPushButton(self.tab_2)
        self.edge_preserving_filter_process_button.setObjectName(u"edge_preserving_filter_process_button")
        sizePolicy4.setHeightForWidth(self.edge_preserving_filter_process_button.sizePolicy().hasHeightForWidth())
        self.edge_preserving_filter_process_button.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.edge_preserving_filter_process_button)

        self.tabWidget.addTab(self.tab_2, "")

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_3.setTitle("")
        self.image_before_label.setText("")
        self.image_after_label.setText("")
        self.upload_before_image_button.setText(QCoreApplication.translate("MainWindow", u"Upload image", None))
        self.mean_filter_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Mean filter", None))
        self.edge_preserving_filter_process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Edge preserving", None))
    # retranslateUi

