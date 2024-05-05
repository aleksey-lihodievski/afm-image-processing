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
        MainWindow.resize(592, 409)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"QLabel {\n"
"	border: 1px solid white;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.image_before_label = QLabel(self.groupBox)
        self.image_before_label.setObjectName(u"image_before_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.image_before_label.sizePolicy().hasHeightForWidth())
        self.image_before_label.setSizePolicy(sizePolicy2)
        self.image_before_label.setStyleSheet(u"")
        self.image_before_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.image_before_label)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.image_after_label = QLabel(self.groupBox)
        self.image_after_label.setObjectName(u"image_after_label")
        sizePolicy2.setHeightForWidth(self.image_after_label.sizePolicy().hasHeightForWidth())
        self.image_after_label.setSizePolicy(sizePolicy2)
        self.image_after_label.setStyleSheet(u"")
        self.image_after_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.image_after_label)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.upload_before_image = QPushButton(self.tab)
        self.upload_before_image.setObjectName(u"upload_before_image")

        self.verticalLayout_2.addWidget(self.upload_before_image)

        self.mean_filter_button = QPushButton(self.tab)
        self.mean_filter_button.setObjectName(u"mean_filter_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mean_filter_button.sizePolicy().hasHeightForWidth())
        self.mean_filter_button.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.mean_filter_button)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 0, 568, 267))
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setStyleSheet(u"QLabel {\n"
"	border: 1px solid white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.image_before_label_2 = QLabel(self.groupBox_2)
        self.image_before_label_2.setObjectName(u"image_before_label_2")
        sizePolicy2.setHeightForWidth(self.image_before_label_2.sizePolicy().hasHeightForWidth())
        self.image_before_label_2.setSizePolicy(sizePolicy2)
        self.image_before_label_2.setStyleSheet(u"")
        self.image_before_label_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.image_before_label_2)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.image_after_label_2 = QLabel(self.groupBox_2)
        self.image_after_label_2.setObjectName(u"image_after_label_2")
        sizePolicy2.setHeightForWidth(self.image_after_label_2.sizePolicy().hasHeightForWidth())
        self.image_after_label_2.setSizePolicy(sizePolicy2)
        self.image_after_label_2.setStyleSheet(u"")
        self.image_after_label_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.image_after_label_2)

        self.upload_before_image_2 = QPushButton(self.tab_2)
        self.upload_before_image_2.setObjectName(u"upload_before_image_2")
        self.upload_before_image_2.setGeometry(QRect(10, 280, 568, 32))
        self.mean_filter_button_2 = QPushButton(self.tab_2)
        self.mean_filter_button_2.setObjectName(u"mean_filter_button_2")
        self.mean_filter_button_2.setGeometry(QRect(40, 320, 568, 32))
        sizePolicy3.setHeightForWidth(self.mean_filter_button_2.sizePolicy().hasHeightForWidth())
        self.mean_filter_button_2.setSizePolicy(sizePolicy3)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.image_before_label.setText("")
        self.image_after_label.setText("")
        self.upload_before_image.setText(QCoreApplication.translate("MainWindow", u"Upload image", None))
        self.mean_filter_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Mean filter", None))
        self.groupBox_2.setTitle("")
        self.image_before_label_2.setText("")
        self.image_after_label_2.setText("")
        self.upload_before_image_2.setText(QCoreApplication.translate("MainWindow", u"Upload image", None))
        self.mean_filter_button_2.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

