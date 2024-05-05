from PyQt6.QtWidgets import QApplication

import sys

from user_interface import UserInterface

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserInterface()

    window.showMaximized()

    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
